from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView, CreateView

from .forms import PrecipitationMeasurementForm, RegisterUserForm, LoginUserForm
from .models import PrecipitationMeasurement, Country, MeasurementSensors, Location
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

	def test_func(self):
		return self.request.user.is_superuser


# Create your views here.


def index(req):
	all_mes = PrecipitationMeasurement.objects.all()
	props = {
		"title": "Главная / Осадки",
		"all_mes": all_mes,
	}
	return render(req, "main/index.html", props)


def countries(req):
	all_cou = Country.objects.all()
	props = {
		"title": "Страны",
		"all_cou": all_cou,
	}
	return render(req, "main/country.html", props)


def sensors(req):
	all_sens = MeasurementSensors.objects.all()
	props = {
		"title": "Датчики",
		"all_sens": all_sens,
	}
	return render(req, "main/sensors.html", props)


def locations(req):
	all_loc = Location.objects.all()
	props = {
		"title": "Локации",
		"all_loc": all_loc,
	}
	return render(req, "main/locations.html", props)


def add_mes(req):
	if not req.user.is_superuser:
		return HttpResponse("<h1>Нет доступа</h1>")

	error = ''
	all_cou = Country.objects.all()
	if req.method == 'POST':
		form = PrecipitationMeasurementForm(req.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = "Ошибка добавления"

	form = PrecipitationMeasurementForm()

	props = {
		"title": "Осадки / Добавить",
		'form': form,
		'error': error,
		"all_cou": all_cou
	}
	return render(req, "main/addMes.html", props)


class PrecipitationMeasurementUpdateView(SuperUserRequiredMixin, UpdateView, ):
	model = PrecipitationMeasurement
	template_name = "main/addMes.html"
	form_class = PrecipitationMeasurementForm
	success_url = "/"


class PrecipitationMeasurementDeleteView(SuperUserRequiredMixin, DeleteView):
	model = PrecipitationMeasurement
	template_name = "main/deleteMes.html"
	success_url = "/"


class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = 'main/register.html'
	success_url = "/"


class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'main/login.html'
	success_url = "/"

	def get_success_url(self):
		return "/"


def logout_user(req):
	logout(req)
	return redirect("login")

import django.forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from .models import PrecipitationMeasurement
from django.forms import ModelForm, NumberInput, DateTimeInput, Select, SelectMultiple, TextInput, PasswordInput


class PrecipitationMeasurementForm(ModelForm):
	class Meta:
		model = PrecipitationMeasurement
		fields = ['longitude', 'latitude', 'width', 'length', 'mm_h', 'date', 'country', "sensors"]
		widgets = {
			'longitude': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Долгота'
			}),
			'latitude': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Широта'
			}),
			'width': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ширина'
			}),
			'length': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Длина'
			}),
			'height': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Высота'
			}),
			'mm_h': NumberInput(attrs={
				'class': "form-control",
				'placeholder': 'Количество осадков(ММ/Ч)'
			}),
			"date": DateTimeInput(attrs={
				'class': "form-control",
				'placeholder': 'Дата и время'
			}),
			"country": Select(attrs={
				'class': "form-control",
			}),
			"sensors": SelectMultiple(attrs={
				'class': "form-control",
			})
		}


class RegisterUserForm(UserCreationForm):
	username = django.forms.CharField(label='Логин', widget=django.forms.TextInput(attrs={'class': 'form-control'}))
	password1 = django.forms.CharField(label='Пароль', widget=django.forms.PasswordInput(attrs={
		'class': 'form-control',
	}))
	password2 = django.forms.CharField(label='Повторить пароль', widget=django.forms.PasswordInput(attrs={
		'class': 'form-control',
	}))

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
	username = django.forms.CharField(label='Логин', widget=django.forms.TextInput(attrs={'class': 'form-control'}))
	password = django.forms.CharField(label='Пароль', widget=django.forms.PasswordInput(attrs={
		'class': 'form-control',
	}))
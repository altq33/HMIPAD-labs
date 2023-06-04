from django.urls import path, include
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
	path('', views.index, name='home'),
	path('add', views.add_mes, name='add'),
	path('delete/<int:pk>', views.PrecipitationMeasurementDeleteView.as_view(), name='delete'),
	path('update/<int:pk>', views.PrecipitationMeasurementUpdateView.as_view(), name='update'),
	path('countries', views.countries, name='countries'),
	path('sensors', views.sensors, name='sensors'),
	path('locations', views.locations, name='locations'),
	path('register', RegisterUser.as_view(), name='register'),
	path('login', LoginUser.as_view(), name='login'),
	path('logout', logout_user, name='logout'),
]

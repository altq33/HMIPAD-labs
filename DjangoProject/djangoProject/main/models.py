from django.db import models

# Create your models here.


class PrecipitationMeasurement(models.Model):
	latitude = models.fields.IntegerField('Широта')
	longitude = models.fields.IntegerField("Долгота")
	width = models.fields.IntegerField("Ширина")
	length = models.fields.IntegerField("Длина")
	mm_h = models.fields.IntegerField("ММ/Ч")
	date = models.fields.DateTimeField("Дата и время")
	country = models.ForeignKey("Country", on_delete=models.PROTECT, null=True)
	sensors = models.ManyToManyField('MeasurementSensors')

	def __str__(self):
		return f'{self.id}'


class Country(models.Model):
	code = models.fields.IntegerField('Код', unique=True)
	name = models.fields.CharField('Название', unique=True, max_length=100)


	def __str__(self):
		return f'{self.name}'


class Location(models.Model):
	measurement = models.OneToOneField(PrecipitationMeasurement, on_delete=models.PROTECT, primary_key=True)
	latitude = models.fields.IntegerField('Широта')
	longitude = models.fields.IntegerField("Долгота")
	sea_height = models.fields.IntegerField("Высота над уровнем моря")
	area = models.fields.IntegerField("Площадь")

	def __str__(self):
		return f'Локация {self.id}'


class MeasurementSensors(models.Model):
	name = models.fields.CharField('Название', unique=True, max_length=100)
	type = models.fields.IntegerField('Тип')

	def __str__(self):
		return f'{self.name}'


class PrecipitationForCountry(models.Model):
	min = models.fields.IntegerField("Минимум")
	max = models.fields.IntegerField("Максимум")
	avg = models.fields.IntegerField("Среднее")
	country = models.OneToOneField(Country, on_delete=models.PROTECT, primary_key=True)
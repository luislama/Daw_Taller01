from djongo import models
# from mongoengine import *
# Create your models here.

class Reporte(models.Model):
	nombre = models.CharField(max_length=60)
	servicio = models.CharField(max_length=15)
	ciudad = models.CharField(max_length=25)
	fecha = models.DateField()
	totalDeFactura = models.IntegerField()

# class Usuario(models.Model):
#	nombreUsuario = models.CharField(max_length=50)
#	servicios = models.ManyToManyField(Servicio)
#
#	def __str__(self):
#		return self.nombreUsuario
#
#	class Meta:
#		ordering = ('nombreUsuario',)
#		abstract = True

# class Servicio(models.Model):
#	nombreServicio = models.CharField(max_length=20)
#	usuarios = models.EmbeddedModelField(
#        model_container=Usuario,
#    )
#
#	def __str__(self):
#		return self.nombreServicio
#
#	class Meta:
#		ordering = ('nombreServicio',)

# class Servicio(EmbeddedDocument):
#	nombreServicio = StringField(max_length=20)
#
#	def __str__(self):
#		return self.nombreServicio
#
#	class Meta:
#		ordering = ('nombreServicio',)

# class Usuario(models.Model):
#	nombreUsuario = StringField(max_length=50)
#	servicios = ListField(EmbeddedDocumentField(Servicio))
#
#	def __str__(self):
#		return self.nombreUsuario
#
#	class Meta:
#		ordering = ('nombreUsuario',)
from django.urls import path

from . import views

urlpatterns = [
	path('usuarios',views.reportes, name='reportes'),
	path('usuarios/$',views.reportes, name='reportes'),
]
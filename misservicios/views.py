from django.shortcuts import render
from django.http import HttpResponse 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Reporte

import dateutil
from dateutil.parser import parse

# Create your views here.

def reportes(request):
	reportes = Reporte.objects.all()
	servicios = Reporte.objects.values('servicio').distinct()
	fechas = Reporte.objects.values('fecha').distinct().order_by('fecha')
	reportesFiltrados = reportes.filter(servicio=servicios[0]['servicio'],fecha=fechas[0]['fecha'])

	if request.method == 'GET':
		servicioSeleccionado = request.GET.get('servicioSeleccionado',servicios[0]['servicio'])
		fechaSeleccionada = request.GET.get('fechaSeleccionada',fechas[0]['fecha'])
		if(fechaSeleccionada!=fechas[0]['fecha']):
			fechaSeleccionada1 = parse(fechaSeleccionada).strftime("%Y-%m-%d")
		reportesFiltrados = reportes.filter(servicio=servicioSeleccionado,fecha=fechaSeleccionada1)
	
	#reportesFiltrados = reportesFiltrados[:500]

	

	return render(request, 'usuarios.html',{'servicios':servicios, 'fechas':fechas,'reportes':reportesFiltrados})
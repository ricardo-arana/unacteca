# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from biblioteca.models import Libro
from django.db.models import Q
from django.utils.encoding import smart_str
from django.views.generic import DetailView

# Create your views here.

def home(request):
	template = loader.get_template('index.html')
	titulo = "Pagina principal"
	context = RequestContext(request, {
        'titulo': titulo,
    })
	return HttpResponse(template.render(context))

def buscar(request):
	query = request.GET.get('rq', '')
	query = smart_str(query)
	titulo = ""
	if query:
		qset = (
			Q(titulo__icontains=query) |
			Q(subtitulo__icontains=query) |
			Q(descripcion__icontains=query)
		)
		resultado = Libro.objects.filter(qset).distinct()
		titulo = str(query)
	else:
		resultado = []
		titulo = "no hay resultado"
	template = loader.get_template('biblioteca/buscar.html')
	context = RequestContext(request,{
		'titulo': titulo,
		'resultado': resultado,
		'query': query,
		})
	return HttpResponse(template.render(context))

def buscar_deuda(request):
	titulo = "Consutlar Deuda"
	template = loader.get_template('biblioteca/buscar_deuda.html')
	context = RequestContext(request,{
		'titulo': titulo,
		})
	return HttpResponse(template.render(context))

def login(request):
	titulo = u"Identificación"
	template = loader.get_template('login.html')
	context = RequestContext(request,{
		'titulo': titulo,
		})
	return HttpResponse(template.render(context))

class detalle(DetailView):

	template_name = 'biblioteca/detalle.html'
	model = Libro
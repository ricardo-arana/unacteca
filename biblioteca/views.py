# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from biblioteca.models import Libro, Ejemplar
from django.db.models import Q
from django.utils.encoding import smart_str
from django.views.generic import DetailView
from django.shortcuts import render_to_response


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


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

def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('usuario/nuevo_usuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def login(request):
	titulo = u"Identificación"
	template = loader.get_template('login.html')
	context = RequestContext(request,{
		'titulo': titulo,
		})
	return HttpResponse(template.render(context))

#def solicitar(request):
#	if request.metho=='POST':


class detalle(DetailView):

	template_name = 'biblioteca/detalle.html'
	model = Libro
	def get_context_data(self, **kwargs):
	    context = super(detalle, self).get_context_data(**kwargs)
	    ejemplares = context['object'].ejemplar_set.filter(estado='d').count()
	    context['disponibles'] = ejemplares
	    return context


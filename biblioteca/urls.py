from django.conf.urls import patterns, url

from biblioteca import views

urlpatterns = patterns('',

    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle.as_view()),

)
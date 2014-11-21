from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'biblioteca.views.home', name='home'),
    url(r'^login/$', 'biblioteca.views.login', name='login'),
	url(r'^deuda/$', 'biblioteca.views.buscar_deuda', name='buscar_deuda'),
    url(r'^biblioteca/', include('biblioteca.urls')),


    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
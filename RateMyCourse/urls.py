from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rate/', include('rate.urls')),
    #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/ico/favicon.ico'}),
)
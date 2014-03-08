from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from portfolio import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'holmes_creative.views.home', name='home'),
    # url(r'^holmes_creative/', include('holmes_creative.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),

    url(r'^$', views.home, name='home'),

    url(r'^sketchbook/', views.sketchbook, name='sketchbook'),
)

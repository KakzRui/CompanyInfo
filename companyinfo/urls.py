from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'companydetails.views.index'),
    url(r'^api/', include('companydetails.urls')),
)

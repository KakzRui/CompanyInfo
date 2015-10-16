from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'companydetails.views.index'),
    url(r'^api/', include('companydetails.urls'))
)
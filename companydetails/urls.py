from django.conf.urls import patterns, include, url
# from rest_framework import routers
from companydetails.views import CompanyList, CompanyListDetail, OwnerList
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^companylist/$', CompanyList, name='company-list'),
	url(r'^companylist/(?P<pk>[0-9]+)/$', CompanyListDetail, name='company-listdetail'),
	url(r'^companylist/(?P<pk>[0-9]+)/ownerlist/$', OwnerList, name='owner-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

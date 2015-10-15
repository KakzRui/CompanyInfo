from django.conf.urls import patterns, include, url
from companydetails.views import CompanyList, CompanyListDetail, OwnerList, OwnerListDetail
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
	url(r'^companylist/$', CompanyList, name='company-list'),
	url(r'^companylist/(?P<pk>[0-9]+)/$', CompanyListDetail, name='company-listdetail'),
	url(r'^companylist/(?P<pk>[0-9]+)/ownerlist$', OwnerList, name='owner-list'),
	# url(r'^companylist/(?P<pk>[0-9]+)/ownerlist/(?P<id>[0-9]+)/$', OwnerListDetail, name='owner-listdetail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
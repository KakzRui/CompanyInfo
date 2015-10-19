from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CompanyDetails, OwnerDetails
from .serializers import CompanySerializer
from django.http import HttpResponse

from rest_framework.decorators import detail_route
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import generics
from django.test.client import RequestFactory
import logging 

######################################### Logger Intialization ###################################################################

logger = logging.getLogger('JSON')

logger.info("Application Started")
####################################### AngularJS Client Template #################################################################

def index(request):
	return render_to_response('index.html', RequestContext(request))


################################## CompanyList method for listing all the companies and adding a company ############################

@api_view(['GET', 'POST'])
@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
def CompanyList(request):
	"""
	List all Companies, or create a new Company.
	"""
	if request.method == 'GET':
		obj = CompanyDetails.objects.all()
		context = dict(request=RequestFactory().get('/'))
		serializer = CompanySerializer(obj, many=True, context=context)
		logger.debug("Companies List: %s", serializer.data)
		return Response(serializer.data)

	elif request.method == 'POST':
		context = dict(request=RequestFactory().get('/'))
		serializer = CompanySerializer(data=request.DATA, context=context)
		if serializer.is_valid(raise_exception=True):
			serializer.validated_data
			serializer.save()
			logger.debug("Successfully added company: %s", serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		logger.error("Couldn't able to add company: %s", serialzer.errors)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###################################### CompanyDetail method for update and delete of each company ##################################

@api_view(['GET', 'PUT', 'DELETE'])
def CompanyListDetail(request, pk):
	"""
	Retrieve, update or delete a Company.
	"""
	try:
		obj = CompanyDetails.objects.get(pk=pk)
		context = dict(request=RequestFactory().get('/'))
	except CompanyDetails.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CompanySerializer(obj, context=context)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CompanySerializer(obj, data=request.data, context=context)
		if serializer.is_valid():
			serializer.save()
			logger.debug("Successfully updated company details: %s", serializer.data)
			return Response(serializer.data)
		logger.error("Couldn't able to update company details: %s", serialzer.errors)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		obj.delete()
		logger.debug("Successfully deleted company: %s", obj)
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)

###################################### OwnerList method is for displaying and adding owners of a company ############################

@api_view(['GET', 'POST'])
def OwnerList(request, pk):
	"""
	List all Owners of the Company, or create new Owner.
	"""
	if request.method == 'GET':
		obj = OwnerDetails.objects.filter(company_id=pk)
		renderer_classes = (renderers.StaticHTMLRenderer,)
		serializer = OwnerSerializer(obj, many=True)
		logger.debug("Owners List: %s", serializer.data)
		return Response(serializer.data)

	elif request.method == 'POST':
		request.DATA['company']=int(pk)
		logger.debug("Data: %s", request.DATA)
		serializer = OwnerSerializer(data=request.DATA)
		if serializer.is_valid(raise_exception=True):
			logger.debug("Successfully added owner to the company:%s", serializer.validated_data)
			serializer.save(company_id=int(pk))
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		logger.error("Couldn't able to add owner to the company: %s", serialzer.errors)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

####################################################################################################################################
###############################################################    END   ###########################################################
####################################################################################################################################		

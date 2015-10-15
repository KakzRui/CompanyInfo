from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CompanyDetails
from .serializers import CompanySerializer
from django.http import HttpResponse

def index(request):
	return render_to_response('index.html', RequestContext(request))

@api_view(['GET', 'POST'])
def CompanyList(request):
	"""
	List all Companies, or create a new Company.
	"""
	if request.method == 'GET':
		obj = CompanyDetails.objects.all()
		serializer = CompanySerializer(obj, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = CompanySerializer(data=request.DATA)
		if serializer.is_valid(raise_exception=True):
			serializer.validated_data
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CompanyListDetail(request, pk):
	"""
	Retrieve, update or delete a Company.
	"""
	try:
		obj = CompanyDetails.objects.get(pk=pk)
	except CompanyDetails.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CompanySerializer(obj)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CompanySerializer(obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		obj.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)

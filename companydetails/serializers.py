from rest_framework import serializers
from .models import CompanyDetails
import logging 

logger = logging.getLogger('JSON')

############################################# Company Serializer ########################################################

class CompanySerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	company_id = serializers.IntegerField()
	name = serializers.CharField(max_length=100)
	address = serializers.CharField(max_length=100)
	city = serializers.CharField(max_length=100)
	country = serializers.CharField(max_length=100)
	email = serializers.EmailField(max_length=100)
	phone = serializers.CharField(max_length=100)
	owners = serializers.HyperlinkedIdentityField(view_name='owner-list', format='html')
		
	class Meta:
	    model = CompanyDetails
	    fields = ('id', 'company_id', 'name', 'address', 'city', 'country', 'email', 'phone', 'owners')

	def create(self, validated_data):
		return CompanyDetails.objects.create(
			company_id = validated_data['company_id'],
			name = validated_data['name'],
			address = validated_data['address'],
			city = validated_data['city'],
			country = validated_data['country'],
			email = validated_data['email'],
			phone = validated_data['phone']
			)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Company` instance, given the validated data.
		"""
		instance.company_id = validated_data.get('company_id', instance.company_id)
		instance.name = validated_data.get('name', instance.name)
		instance.address = validated_data.get('address', instance.address)
		instance.city = validated_data.get('city', instance.city)
		instance.country = validated_data.get('country', instance.country)
		instance.email = validated_data.get('email', instance.email)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.save()
		return instance

############################################# Owner Serializer #############################################################

class OwnerSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	company_id = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
	name = serializers.CharField(max_length=100)

	class Meta:
	    model = OwnerDetails
	    fields = ('id', 'company_id', 'name')

	def create(self, validated_data):
		logger.debug("Serializers validated data: %s", validated_data)
		return OwnerDetails.objects.create(
			company_id = validated_data['company_id'],
			name = validated_data['name'],
			)

	# def update(self, instance, validated_data):
	# 	"""
	# 	Update and return an existing `Company` instance, given the validated data.
	# 	"""
	# 	instance.company_id = validated_data.get('company_id', instance.company_id)
	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.save()
	# 	return instance

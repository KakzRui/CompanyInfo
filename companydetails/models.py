from django.db import models

# Create your models here.
class CompanyDetails(models.Model):
	id = models.AutoField(primary_key=True)
	company_id = models.IntegerField(unique=True, null=False, blank=False)
	name = models.CharField(unique=True, max_length=100, null=False, blank=False)
	address = models.CharField(max_length=1000, null=False, blank=False)
	city = models.CharField(max_length=100, null=False, blank=False)
	country = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField(unique=True, null=True, blank=True)
	phone = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		verbose_name = 'Company Details'

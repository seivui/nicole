from django.db import models

from django.utils.encoding import smart_unicode

# Create your models here.
class Household(models.Model):
	household_name = models.CharField(max_length=120, null=False, blank=False, primary_key=True)

class User(models.Model):
	user_name = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
	first_name = models.CharField(max_length=120, null=False, blank=False)
	last_name = models.CharField(max_length=120, null=False, blank=False)
	household_name = models.ForeignKey('Household')
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)

class Wallet(models.Model):
	user_name = models.ForeignKey('User', primary_key=True)
	balance = models.DecimalField(max_digits=50, decimal_places=2)
	




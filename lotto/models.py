from django.db import models

# Create your models here.
class Saledata(models.Model):
	lnochar = models.CharField(max_length=2)
	lnoint = models.CharField(max_length=6)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	reseller = models.ForeignKey('auth.User',related_name='reseller',on_delete=models.CASCADE)
	cname = models.CharField(max_length=100)
	cadress = models.CharField(max_length=100)
	ccontact = models.CharField(max_length=50)
	nth=models.CharField(max_length=50,default=True)
	def __str__(self):
		return self.lnochar+" "+self.lnoint
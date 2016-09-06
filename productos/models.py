from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
	category=models.CharField(max_length=100)
	

	def __str__(self):
		return self.category

class Subcat(models.Model):
	sub=models.CharField(max_length=100)
	

	def __str__(self):
		return self.sub

class Product(models.Model):
	name=models.CharField(max_length=140)
	cat=models.ForeignKey(Category, related_name='cat', null=True)
	subcat=models.ForeignKey(Subcat, related_name='subcat', null=True)
	image=models.ImageField(upload_to='images')
	price=models.IntegerField()
	in_stock=models.BooleanField(default=True)
	desc=models.TextField()
	slug=models.SlugField(max_length=280)

	def get_absolute_url(self):
		return reverse('products:detalle', args=[self.slug])


	def __str__(self):
		return self.name


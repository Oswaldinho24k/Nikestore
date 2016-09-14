from django.db import models
from django.conf import settings 

# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	phone_number=models.CharField(max_length=10)
	birth=models.DateField()
	photo=models.ImageField(upload_to="users/%Y/%m/%d",blank=True)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)

class Address(models.Model):
	
	city=models.CharField(max_length=100)
	street=models.CharField(max_length=100)
	number=models.IntegerField()
	colony=models.CharField(max_length=100)
	zip_code=models.IntegerField()

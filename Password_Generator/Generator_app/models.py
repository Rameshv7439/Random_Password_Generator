from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50)

class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile= models.CharField(max_length=20)
    status= models.CharField(max_length=20,null=True)
    con_password= models.CharField(max_length=20,null=True)


class PasswordSafe(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	platform = models.CharField(max_length = 20, null = False, blank = True)
	Password = models.CharField(max_length = 20, null = False, blank = False)

	def __str__(self):
		return self.platform
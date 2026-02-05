from django.db import models

# Create your models here.
class empinfo(models.Model):
       id=models.IntegerField(primary_key=True ,auto_created=True)
       name=models.CharField(max_length=220)
       designation=models.CharField(max_length=220)
       email=models.EmailField(max_length=100)
       salary=models.IntegerField()
from collections import UserDict
from django.db import models

class Trainers(models.Model):
   trainer_name=models.CharField(max_length=255)
   trainer_dept=models.CharField(max_length=255)
   trainer_image=models.ImageField(upload_to='trainers')
   
class Admission(models.Model):
   name=models.CharField(max_length=255)
   phone=models.CharField(max_length=10)
   email=models.EmailField()
   admission_date=models.DateField()
   
   
class Payment(models.Model):
   Person_name=models.CharField(max_length=20)
   card_number=models.CharField(max_length=15)
   expiry=models.DateField()
   cvv=models.CharField(max_length=3)
   







    

class otp(models.Model):
    code = models.CharField(max_length=4)

    
from django.db import models

# Create your models here.


class Account(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    governorate=models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=20)
    job=models.CharField(max_length=50 ,default='none')
    def __str__(self):
        return self.name

class ClintOrder(models.Model):
    cus_name=models.CharField(max_length=255)
    cus_phone=models.CharField(max_length=255)
    tech_phone=models.CharField(max_length=255)
    o_desc=models.CharField(max_length=255)
    o_date=models.CharField(max_length=255)
    tech_name=models.CharField(max_length=255)
    o_status=models.CharField(max_length=255)
    o_excute_date=models.CharField(max_length=255)
    o_governorate=models.CharField(max_length=255)
    o_region=models.CharField(max_length=255)



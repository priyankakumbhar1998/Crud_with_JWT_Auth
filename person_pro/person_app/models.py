from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=GENDER)
    contact_no = PhoneNumberField(region="IN")
    aadhar_no = models.CharField(max_length=12)


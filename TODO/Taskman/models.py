from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
# Create your models here.

class TODO(models.Model):
    status_choises = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choises = [
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
    ('5', '5th'),
    ('6', '6th'),
    ('7', '7th'),
    ('8', '8th'),
    ('9', '9th'),
    ('10', '10th'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 ,
    choices= status_choises)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    date = models.DateTimeField( auto_now_add=True)
    # deadline = models.DateTimeField(default=timezone.now)
    # deadline = models.DateTimeField( auto_now=False , auto_now_add=True)
    priority = models.CharField(max_length=2 , 
    choices= priority_choises)
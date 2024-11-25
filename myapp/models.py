from django.db import models
from django.utils import timezone

from loginapp.models import Userprofile

# Create your models here.

class Restaurant_model(models.Model):
    login_id = models.OneToOneField(Userprofile, on_delete=models.CASCADE, blank=True, null=True)
    restaurantName = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)



class Complaint_model(models.Model):
    complaint = models.CharField(max_length=100, null=True, blank=True)
    reply = models.CharField(max_length=100, null=100, blank=True)

class Notification_model(models.Model):
    notification = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class FoodInformation_model(models.Model):
    foodCategory = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    foodStatus = models.CharField(max_length=100, null=True, blank=True)
    foodName = models.CharField(max_length=100, null=True, blank=True)


class CampRegistrationModel(models.Model):
    login_id = models.OneToOneField(Userprofile, on_delete=models.CASCADE, null=True, blank=True)
    campname = models.CharField(max_length=100, null=True, blank=True)
    campno = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    proof = models.FileField(upload_to='proof/', null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

class Donation_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    item = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.CharField(max_length=100, null=True, blank=True)

class Clothes_model(models.Model):
    clothes = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
from django.forms import ModelForm

from .models import *


class Register_form(ModelForm):
    class Meta:
        model = Restaurant_model
        fields = ['restaurantName','location','phoneNumber','type','pincode','state', 'about']

class Complaint_form(ModelForm):
    class Meta:
        model = Complaint_model
        fields = ['complaint', 'reply']


class Reply_form(ModelForm):
    class Meta:
        model = Complaint_model
        fields = ['reply']

class Notification_form(ModelForm):
    class Meta:
        model = Notification_model
        fields = ['notification']

class FoodInformation_form(ModelForm):
    class Meta:
        model = FoodInformation_model
        fields = ['foodCategory', 'description', 'foodStatus', 'foodName']


class Campregistration_form(ModelForm):
    class Meta:
        model = CampRegistrationModel
        fields = ['campname', 'campno', 'place', 'proof', 'status']

class Clothes_form(ModelForm):
    class Meta:
        model = Clothes_model
        fields = ['clothes', 'category']
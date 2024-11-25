from django.contrib import admin

from .models import  *

# Register your models here.

admin.site.register(Restaurant_model)
admin.site.register(Complaint_model)
admin.site.register(Notification_model)
admin.site.register(FoodInformation_model)
admin.site.register(CampRegistrationModel)
admin.site.register(Donation_model)
admin.site.register(Clothes_model)
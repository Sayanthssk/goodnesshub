from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Complaint_model, FoodInformation_model, Notification_model



from .forms import *

# Create your views here.

class Restaurant(View):
    def get(self, request):
        return render(request,'register.html')
    
    def post(self, request):
        c = Register_form(request.POST)
        if c.is_valid():
            g = c.save(commit=False)
            a = Userprofile.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                user_type='RESTAURANT',
                status = 'ACTIVE'
            )
            g.login_id = a
            g.save()
            
            return redirect('login')
        
class Restaurant_view(View):
    def get(self, request):
        c = Restaurant_model.objects.select_related('login_id').all()
        return render(request, 'restaurantView.html', { 's':c })
    
        
# class Profile(View):
#     def get(self, request):
#         c = User.objects.all()
#         return render(request, 'profile.html', {'s' : c})


class Feedback(View):
    def get(self, request):
        return render(request, 'feedback.html')
    
    def post(self, request):
        c = Complaint_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('view_complaint')
        
class View_complaint(View):
    def get(self, request):
        c = Complaint_model.objects.all()
        return render(request, 'viewFeedback.html',{'s':c})
    

class Reply(View):
    def get(self, request, pk):
        feedback = get_object_or_404(Complaint_model, pk = pk)
        print(feedback)
        return render(request, 'reply.html', {'feedback': feedback})
    
    def post(self, request, pk):
        
        feedback = get_object_or_404(Complaint_model, pk = pk)
        form = Reply_form(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('view_complaint')

class Notification(View):
    def get(self, request):
        return render(request, 'sendNotification.html')
    
    def post(self, request):
        c = Notification_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('viewNotification')
        
class View_notification(View):
    def get(self, request):
        c = Notification_model.objects.all()
        return render(request, 'viewNotification.html', {'a' : c})
     
class Delete_Notification(View):
    def get(self, request, pk):
        notification = get_object_or_404(Notification_model, pk = pk)
        notification.delete()
        return HttpResponse('''<script>alert('delete successfully'); window.location.href='/viewNotification/'</script>''')
    

class FoodInformation(View):
    def get(self, request):
        return render(request, 'foodDescription.html')
    
    def post(self, request):
        c = FoodInformation_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('foodInformationview')
        
class View_foodInformation(View):
    def get(self, request):
        c = FoodInformation_model.objects.all()        
        return render(request, 'FoodInformationVIew.html', { 'b':c })
    

class Delete_foodInformation(View):
    def get(self, request, pk):
        foodInformation = get_object_or_404(FoodInformation_model, pk=pk)
        foodInformation.delete()
        return HttpResponse('''<script>alert('delete successfully'); window.location.href='/foodInformationview/'</script>''')

class Edit_foodInformation(View):
    def get(self, request, pk):
        foodInformation = get_object_or_404(FoodInformation_model, pk=pk)
        return render(request, 'editFoodInformation.html', {'foodInformation': foodInformation})
    
    def post(self, request, pk):
        foodInformation = get_object_or_404(FoodInformation_model, pk=pk)
        c = FoodInformation_form(request.POST, instance=foodInformation)
        if c.is_valid():
            c.save()
            return redirect('foodInformationview')
        
class CampRegistration(View):
    def get(self, request):
        return render(request, 'CampRegistration.html')

    def post(self, request):
        c = Campregistration_form(request.POST, request.FILES)
        
        if c.is_valid():
            g = c.save(commit=False)
            a = Userprofile.objects.create_user(
                username=request.POST['username'],  
                password=request.POST['password'],
                user_type='CAMP',
                status = 'ACTIVE'
            )
            g.login_id = a
            g.save()
            
            return redirect('login')
        
class Camp_view(View):
    def get(self, request):
        c = CampRegistrationModel.objects.all()
        return render(request, 'camp_view.html', {'s':c})
        
class View_donation(View):
    def get(self, request):
        c = Donation_model.objects.all()
        return render(request, 'donation_view.html', { 's':c })
    

class Delete_donation(View):
    def get(self, request, pk):
        donation = get_object_or_404(Donation_model, pk=pk)
        donation.delete()
        return HttpResponse('''<script>alert('delete successfully'); window.location.href='/viewdonation/'</script>''')


class Verify_Rest(View):
    def get(self, request, pk):
        c = Restaurant_model.objects.filter(id = pk).first()
        c.login_id.status = 'ACTIVE'
        c.login_id.save()
        return redirect('restaurantview')
    
class Reject_rest(View):
    def get(self, request, pk):
        c = Restaurant_model.objects.filter(id = pk).first()
        c.login_id.status = 'DEACTIVE'
        c.login_id.save()
        return redirect('restaurantview')
    

class Restaurant_profile(View):
    def get(self, request, pk):
        c = Restaurant_model.objects.filter(login_id__id = pk).first()
        return render(request, 'restaurant_profile.html', {'s':c})
    
class Camp_profile(View):
    def get(self, request, pk):
        # Retrieve the camp profile using the primary key (pk)
        camp_profile = get_object_or_404(CampRegistrationModel, pk=pk)
        
        # Pass the camp_profile to the template for rendering
        return render(request, 'camp_profile.html', {'camp_profile': camp_profile})
    

class Add_clothes(View):
    def get(self,request):
        return render(request, 'addClothes.html')
    def post(self, request):
        c = Clothes_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('viewclothes')
        
class View_clothes(View):
    def get(self, request):
        clothes = Clothes_model.objects.all()
        return render(request, 'viewClothes.html',{'clothes':clothes})
    

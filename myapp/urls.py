

from django.urls import path

from .views import  *
urlpatterns = [
    path('restaurant/', Restaurant.as_view(), name='restaurant'),
    path('restaurantview/', Restaurant_view.as_view(), name='restaurantview'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('view_complaint/', View_complaint.as_view(), name='view_complaint'),
    path('reply_feedback/<int:pk>/', Reply.as_view(), name='reply'),
    path('notification/', Notification.as_view(), name='notification'),
    path('viewNotification/', View_notification.as_view(), name='viewNotification'),
    path('deletenotification/<int:pk>/',Delete_Notification.as_view(), name='deletenotification'),
    path('foodInformation/', FoodInformation.as_view(), name='foodInformation'),
    path('foodInformationview/', View_foodInformation.as_view(), name='foodInformationview'),
    path('deletefoodinfromation/<int:pk>/', Delete_foodInformation.as_view(), name='deletefoodinformation'),
    path('editfoodInformation/<int:pk>/', Edit_foodInformation.as_view(), name='editfoodInformation'),
    path('campregistration/', CampRegistration.as_view(), name='campregistration'),
    path('campview/', Camp_view.as_view(), name='campview'),
    path('viewdonation/', View_donation.as_view(), name='viewdonation'),
    path('deletedonation/<int:pk>/', Delete_donation.as_view(), name='deletedonation'),
    path('accept/<int:pk>/', Verify_Rest.as_view(), name='accept'),
    path('reject/<int:pk>/', Reject_rest.as_view(), name='reject'),
    path('restprofile/<int:pk>/', Restaurant_profile.as_view(), name='restprofile'),
    path('addclothes/', Add_clothes.as_view(), name='addclothes'),
    path('viewclothes/', View_clothes.as_view(), name='viewclothes')
    # path('login/', Login.as_view(), name='login'),
]

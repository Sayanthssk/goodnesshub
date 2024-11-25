from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import   *


urlpatterns = [
    path('admindashboard/', Admin_dashboard.as_view(),name='admindashboard'),
    path('login/', UserLogin.as_view(), name='login'),
    path('camp/', Camp.as_view(), name='camp'),
    path('restaurantdash/', Restaurant_dash.as_view(), name='rest'),
    path('', Index.as_view(), name='index'),

]



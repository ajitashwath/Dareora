from django.urls import path
from userprofile import views

urlpatterns = [
    path("",views.user_profile)
]
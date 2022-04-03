from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('singup/',views.sing_up,name='sing_up'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_user,name='logout_user'),
    path('changeprofile/',views. user_profile,name='changeprofile'),
]

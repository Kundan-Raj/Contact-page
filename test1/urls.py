from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name='home'),
    path('register/',views.registerView, name='register_url'),
   
]
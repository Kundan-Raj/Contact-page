from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView,name='home'),
    path('register/',views.registerView, name='register_url'),
   # path(r'^user/create/$',views.create_user,name='create_user'),
    #path('ajax-posting/', views.ajax_posting, name='ajax_posting'),
   
]
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.indexView,name='home'),
    path('register/',views.registerView, name='register_url'),
    url(r'^api/test1$',views.contact_list), #r tells django raw regular pattern
    url(r'^api/test1/(?P<pk>[0-9]+)$', views.contact_detail),
   # path(r'^user/create/$',views.create_user,name='create_user'),
    #path('ajax-posting/', views.ajax_posting, name='ajax_posting'),
   
]
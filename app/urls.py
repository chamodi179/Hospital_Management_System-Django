from app import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Services', views.Services, name='Services')
]
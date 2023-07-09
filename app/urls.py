from app import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Services', views.Services, name='Services'),
    path('services/cosmetic/', views.cosmetic_view, name='cosmetic'),
    path('services/BC_CENTRE/', views.BC_CENTRE_view, name='BC_CENTRE'),
    path('services/GASTROENTEROLOGY/', views.GASTROENTEROLOGY_view, name='GASTROENTEROLOGY'),
    path('services/HEALTH_CHECK/', views.HEALTH_CHECK_view, name='HEALTH_CHECK'),
    path('services/KIDNE_CARE_C/', views.KIDNE_CARE_C_view, name='KIDNE_CARE_C'),
    path('services/FERTILITY_CENTRE/', views.FERTILITY_CENTRE_view, name='FERTILITY_CENTRE'),
    path('services/HEART_CENTRE/', views.HEART_CENTRE_view, name='HEART_CENTRE'),
    path('services/W_WELLNESS/', views.W_WELLNESS_view, name='W_WELLNESS'),
    path('services/UROLOGY_CARE_C/', views.UROLOGY_CARE_C_view, name='UROLOGY_CARE_C'), 
    path('services/MENS_WELLNESS_C/', views.MENS_WELLNESS_C_view, name='MENS_WELLNESS_C'),
    path('go_back/', views.go_back, name='go_back'),
]
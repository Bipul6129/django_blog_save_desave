from django.urls import path
from .import views

urlpatterns = [
    path('',views.landing,name='landing-index'),
    path('logout/',views.logout,name='logout'),
    
    
]
from django.urls import path
from .views import BlogCreateView,BlogListView,BlogDetailView, BlogUpdateView
from . import views

urlpatterns = [
    path('upload-blog/',BlogCreateView.as_view(),name='upload-blog'),
    path('login-home/',views.loginhome,name='login-home'),
    path('detail-view/<int:pk>/',BlogDetailView.as_view(),name='blog-detail'),
    path('save-blog/',views.saveblog,name='save-blog'),
    path('remove-blog/',views.removeblog,name='remove-blog'),
    path('blog-update/<int:pk>/',BlogUpdateView.as_view(),name='blog-update'),
    
]
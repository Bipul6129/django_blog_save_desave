from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as dj_logout
from blog.models import Post_blog
from .filters import BlogFilter
from django.views.generic import ListView
from django_filters.views import FilterView
# Create your views here.

def landing(request):
    user=request.user
    context = {
        
    }
    if user.is_authenticated:
        return redirect('login-home')
    return render(request,'landing/landing-index.html',context)




@login_required
def logout(request):
    dj_logout(request)
    return redirect('landing-index')



    
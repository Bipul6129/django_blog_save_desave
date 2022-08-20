from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as dj_logout
# Create your views here.

def landing(request):
    user=request.user
    if user.is_authenticated:
        return redirect('login-home')
        
    context={
        'title':'Blog-Home'
    }
    return render(request,'landing/landing-index.html',context)




@login_required
def logout(request):
    dj_logout(request)
    return redirect('landing-index')


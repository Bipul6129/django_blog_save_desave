from django.shortcuts import render,redirect
from .forms import RegisterationForm,AccountAuthenticationForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login,authenticate

# Create your views here.

def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect('login-home')
    if request.POST:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing-index')
        else:
            context={
                'signup_form':form
            }
    else:
        form = RegisterationForm()
        context = {
            'signup_form':form
        }
    return render(request,'account/signup.html',context)


def signin(request):
    context = {}
    user=request.user
    if user.is_authenticated:
        return redirect('landing-index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                dj_login(request, user)
                return redirect('login-home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request,'account/signin.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form':u_form
    }
    return render(request,'account/profile.html',context)

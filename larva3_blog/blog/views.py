from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BlogUpload,BlogUpdate
from django.contrib.auth.models import User
from account.models import Account
from .models import Blogs
from larva_3.settings import AUTH_USER_MODEL as CustomUser
# Create your views here.

@login_required
def upload_blog(request):
    user=request.user
    if request.method== 'POST':
        blog_form=BlogUpload(request.POST,request.FILES)
        if blog_form.is_valid():
            obj=blog_form.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            obj.author=author
            obj.save()
            return redirect('home')
    else:            
        blog_form = BlogUpload(request.POST)
    context = {
        'blog_form': blog_form
    }
    return render(request,'blog/upload_blog.html',context)


@login_required
def manage_blog(request):
    user=request.user
    user_blogs=Blogs.objects.filter(author=user.id)
    context = {
        'user_blogs':user_blogs
    }
    return render(request,'blog/manage_blog.html',context)


@login_required
def update_blog(request):
    user=request.user
    if request.method == 'POST':
        blog_id=request.GET.get('id')
        get_blog=Blogs.objects.filter(id=blog_id).first() 
        blog_form=BlogUpdate(request.POST,request.FILES,instance=get_blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('manage_blog')
        else:
        
            return render(request,'blog/update_blog.html',{'blog_form':BlogUpdate(instance=get_blog)})
        
    elif request.GET.get('id'):
        blog_id=request.GET.get('id')
        get_blog=Blogs.objects.filter(id=blog_id).first() 

        if(get_blog):
            if get_blog.author != user:
                return redirect('manage_blog')
            else:
                blog_form=BlogUpdate(instance=get_blog)
                context = {
                    'blog_form':blog_form
                }
                return render(request,'blog/update_blog.html',context)
        else:
            return redirect('home')

    else:
        return redirect('home')
        

@login_required
def delete_blog(request):
    user=request.user
    if request.GET.get('id'):
        blog_id=request.GET.get('id')
        get_blog = Blogs.objects.filter(id=blog_id).first()

        if get_blog:
            if get_blog.author !=user:
                return redirect('manage_blog')
            else:
                get_blog.delete()
                return redirect('manage_blog')
        else:
            return redirect('manage_blog')
    else:
        return redirect('manage_blog')

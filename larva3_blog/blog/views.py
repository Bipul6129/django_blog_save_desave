from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post_blog,User_Blog

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.


class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post_blog
    template_name = 'blog/post_form.html'
    fields = ['title','image','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogListView(ListView):
    model=Post_blog
    template_name = 'landing/login-home.html'
    context_object_name='posts'
    ordering = ['-date']

class BlogDetailView(DetailView):
    model=Post_blog
    template_name='blog/detail-view.html'

def saveblog(request):
    if request.method=='GET':
        user=request.user
        blog_id=request.GET.get('id')
        blog=Post_blog.objects.get(pk=blog_id)
        if blog:
            save = User_Blog(blog=blog,author=user)
            save.save()
        else:
            return redirect('login-home')
    return redirect('login-home')

def removeblog(request):
    if request.method=='GET':
        user=request.user
        blog_id=request.GET.get('id')
        blog_d=Post_blog.objects.get(id=blog_id)
        blog=User_Blog.objects.get(author=user,blog=blog_d)
        blog.delete()
        return redirect('login-home')
    return redirect('login-home')





def loginhome(request):
    user=request.user
    user_saved=user.user_blog_set.filter(author=user)
    exclude_list=[]

    for saved in user_saved:
        exclude_list.append(saved.blog.title)
    selected = Post_blog.objects.exclude(title__in=exclude_list)
                

    
    

    context={
        'posts': selected,
        'saved':user_saved
    }
    return render(request,'landing/login-home.html',context)
from django.contrib import admin
from .models import Post_blog,User_Blog
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    search_fields = ('title','content',)

    

admin.site.register(Post_blog,PostAdmin)



admin.site.register(User_Blog)


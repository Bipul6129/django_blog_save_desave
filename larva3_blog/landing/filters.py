import django_filters
from blog.models import Post_blog

class BlogFilter(django_filters.FilterSet):
    class Meta:
        model=Post_blog
        fields=['title']
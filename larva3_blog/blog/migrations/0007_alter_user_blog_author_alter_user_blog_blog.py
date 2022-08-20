# Generated by Django 4.0.6 on 2022-08-20 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_user_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_blog',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_blog',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.post_blog'),
        ),
    ]

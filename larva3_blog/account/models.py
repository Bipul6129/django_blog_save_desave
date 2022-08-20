from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,username,password=None):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        if not firstname:
            raise ValueError("Enter firstname please")
        if not lastname:
            raise ValueError("Enter lastname please")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,firstname,lastname,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            firstname=firstname,
            lastname=lastname,
            
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    firstname = models.CharField(max_length=15,unique=False)
    lastname = models.CharField(max_length=15,unique=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email' #login with email
    REQUIRED_FIELDS =  ['username','firstname','lastname'] #required when registering

    objects = MyAccountManager()

    def __str__(self):
        return self.email + "," + self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

   

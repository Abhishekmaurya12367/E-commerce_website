from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Accountmanager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email,password=None):
        if not email:
            raise ValueError('email required')
        if not username:
            raise ValueError('username very important ')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,first_name,last_name,email,password):
        user=self.create_user(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

            

class Accounts(AbstractBaseUser):
    username = models.CharField(max_length=150, default="user")
    first_name=models.CharField(max_length=50,unique=True)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=48,unique=True)
    phone_number=models.CharField(max_length=10,unique=True)
    joind_time=models.DateTimeField(auto_now_add=True)
    login_last=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    object=Accountmanager()
    def __str__(self):
       return self.email


    def has_perm(self, perm, obj=None):
      return self.is_admin


    def has_module_perms(self, app_label):
       return True


      
    
     

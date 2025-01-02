from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must provide email address')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,first_name,last_name,username,email,password=None):
       user = self.create_user(
           first_name=first_name,
           email=self.normalize_email(email),
           last_name=last_name,
           username=username,
       )
       user.is_admin=True
       user.is_active = True
       user.is_staff = True
       user.is_superadmin = True
       user.save(using = self._db)
       return user
        

class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (RESTAURANT,'Restaurant'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    role = models.PositiveBigIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
    
    
    #required_fields
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perm(self,app_lable):
        return True
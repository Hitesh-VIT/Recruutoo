# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
       
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
  

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

class CompanyInfo(models.Model):
	company_name_image=models.ImageField(upload_to='Images/Pics',null=True, blank=True)
	company_account=models.OneToOneField(MyUser,null=True, blank=True)
	company_logo=models.ImageField(upload_to='Images/',null=True, blank=True)
	company_name=models.TextField(max_length=255,blank=True,null=True)
	company_url=models.URLField()
	company_email=models.EmailField(null=True, blank=True)
	company_mobile=models.IntegerField(null=True, blank=True)




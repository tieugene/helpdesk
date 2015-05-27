# -*- coding: utf-8 -*-
'''
user.models
Powered by https://docs.djangoproject.com/en/1.6/topics/auth/customizing/#auth-custom-user
'''

# 1. django
#from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# 2. 3rd parties

# 3. system

# 4. local

class HDUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user

class	HDUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', max_length=254, unique=True,)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = HDUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

"""
class	RegQueue(models.Model):
	'''
	Queue of registering requests
	'''
	email
	password
	firstname
	lastname

class	Profile(models.Model):
	'''
	User profile
	'''
	firstname
	midname
	lastname
	phone

class	Role(models.Model):
	'''
	Admin == superuser
	User == <default>
	Assignee == Can get issue
	Monitor = Can view all of issues
	'''
"""
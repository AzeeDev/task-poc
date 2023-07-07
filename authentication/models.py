# from django.db import models
# from baselayer.basemodel import LogsMixin
# from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, AbstractUser)
#
#
# # Create your models here.
#
# class User(AbstractBaseUser, PermissionsMixin, LogsMixin):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
#
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#
#     @property
#     def full_name(self):
#         return "%s %s" % (self.first_name, self.last_name)

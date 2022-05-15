from django.db import models


# Create your models here.

class User(models.Model):
    """ 用户表"""
    username = models.CharField(verbose_name='用户名', max_length=16, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16)

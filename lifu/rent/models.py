
# _*_ coding: utf-8 _*_
from django.db import models
# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=20, default='')
    name = models.CharField(max_length=10, default='')
    sex = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=20, default='')
    sign = models.CharField(max_length=5, default='')


# class Gener(models.Model):
#     generNo = models.CharField(max_length=20)
#     generName = models.CharField(max_length=50)
#

class Cloth(models.Model):
    clothName = models.CharField(max_length=50)
    cloth_price = models.CharField(max_length=50, default='')
    rent_price = models.CharField(max_length=50, default='')
    count = models.IntegerField(max_length=50)
    picture = models.ImageField(upload_to='picture/', default='picture/no-img.jpg')
    type = models.CharField(max_length=50, default='')


class Order(models.Model):
    # 字段解释
    clothName = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default='')
    count = models.IntegerField(max_length=20)
    money = models.CharField(max_length=20)
    order_time = models.CharField(max_length=20)
    orderState = models.CharField(max_length=20)
    rent_time = models.CharField(max_length=20)
    cus_name = models.CharField(max_length=20) # 顾客名
    address= models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Feedback(models.Model):
    email = models.EmailField(max_length=20, default='')
    content = models.TextField()




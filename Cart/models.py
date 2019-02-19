from django.db import models
from User.models import *
from Product.models import *

# Create your models here.
# cart id user_id(F) product_id(F)  quantity checked(是否选择，1表示选择，0表示未选择)
# create_time update_time

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id')
    quantity = models.IntegerField('数量')
    checked = models.BooleanField('是否选择',default=False) #是否选择，1表示选择，0表示未选择
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    
    

#order id user_id(F)  order_No receiver_name receiver_phone receiver_address  create_time  update_time

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    order_No = models.IntegerField('订单号')
    receiver_name = models.CharField('收件人',max_length=30)
    receiver_phone = models.CharField('收件人电话',max_length=11)
    receiver_address = models.CharField('收件人地址',max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    
    def __str__(self):
        return self.order_No
    
    

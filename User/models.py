from django.db import models

# Create your models here.
# user id username password email phone create_time  update_time

class User(models.Model):
    username = models.CharField('用户名',max_length=30,null=False)
    password = models.CharField('密码',max_length=100,null=False)
    email = models.EmailField('邮箱')
    phone = models.CharField('电话',max_length=11)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now_add=True)
    
    def __str__(self):
        return self.username



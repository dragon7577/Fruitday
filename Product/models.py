from django.db import models

# Create your models here.
# category id name status create_time  update_time

class Category(models.Model):
    name = models.CharField('类别名称',max_length=50,null=False)
    status = models.BooleanField('类别状态',default=True) #类别1 正常 类别0 下架
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
# product id category_id(F) name image detail price(decimal(20,2)) status
#  create_time update_time

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField('产品名称',max_length=50,null=False)
    image = models.ImageField('产品图片',upload_to='static/images')
    detail = models.TextField('产品描述',default='产品详情')
    price = models.DecimalField('价格',max_digits=20,decimal_places=2,blank=True)
    status = models.BooleanField('产品状态',default=True) # 1 在售  0 下架
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    
    def __str__(self):
        return self.name

class Banner(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField('Banner',max_length=30)
    image = models.ImageField('轮播图',upload_to='static/images')
    detail = models.TextField('产品描述', default='产品详情')
    status = models.BooleanField('产品状态', default=True)  # 1 在售  0 下架

    def __str__(self):
        return self.name


class DetailPage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=50, null=False)
    image = models.ImageField('图片',upload_to='static/images')
    detail = models.TextField('描述', default='产品详情')
    status = models.BooleanField('产品状态', default=True)  # 1 在售  0 下架

    def __str__(self):
        return self.name


    
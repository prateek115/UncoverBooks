from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Product(models.Model):
    product_id = models.AutoField
    Index = models.IntegerField(default=0)
    product_name = models.CharField(max_length=500,default="")
    product_desc = models.CharField(max_length=200000,default="")
    author_name = models.CharField(max_length=300,default="")
    genre = models.CharField(max_length=100,default="")
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="UncoverBooks/images",default="")

    def __str__(self):
        return str(self.product_name)


class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    desc = models.TextField(max_length=5000,default="")


class Orders(models.Model):
    ord_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address1 = models.CharField(max_length=1000, default="")
    address2 = models.CharField(max_length=1000, default="")
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=10,default="")
    amount = models.IntegerField(default=0)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=4000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class ProductComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:7] + "..."
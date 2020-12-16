from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    code = models.CharField(max_length=30)
    stock_size = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

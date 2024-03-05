from django.db import models


class Product(models.Model):
    product_code = models.CharField(max_length=180)
    product_name = models.CharField(max_length=180)
    unit_price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=180)
    company = models.CharField(max_length=180)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

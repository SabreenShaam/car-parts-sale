from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):
    product_code = models.CharField(max_length=180)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    total_cost = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_code

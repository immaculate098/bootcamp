from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True)
    doll_name = models.CharField(max_length=50, null=False, blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.doll_name

class Sale(models.Model):
    branch_name = models.CharField(max_length=100, null=True, blank=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    amount_received = models.IntegerField(null=False, blank=False)
    issued_to = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(default=timezone.now)

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    def __str__(self):
        return self.item.doll_name

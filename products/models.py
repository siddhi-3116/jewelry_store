from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    JEWELRY_TYPES = [
        ('ring', 'Ring'),
        ('necklace', 'Necklace'),
        ('earring', 'Earring'),
        ('bracelet', 'Bracelet'),
    ]
    
    METAL_TYPES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('platinum', 'Platinum'),
        ('rose_gold', 'Rose Gold'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    jewelry_type = models.CharField(max_length=20, choices=JEWELRY_TYPES)
    metal_type = models.CharField(max_length=20, choices=METAL_TYPES, blank=True)
    gemstone = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products/')
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Product(models.Model):
    titleProduct = models.CharField(max_length=150)
    imgProduct = models.CharField(max_length=255)
    category = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=False)  # max_digits y decimal_places ajustados
    discount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  # Para descuentos en porcentaje
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.titleProduct

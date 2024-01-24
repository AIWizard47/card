from django.db import models

class Card(models.Model):
    PRODUCT_TYPES = [
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        # Add more product types as needed
    ]

    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=1000)
    product_photo_url = models.CharField(max_length=200)
    product_price = models.PositiveIntegerField()
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)

    def __str__(self):
        return self.product_name

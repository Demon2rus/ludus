from django.db import models

class Product(models.Model): #Товар
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    price = models.PositiveIntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


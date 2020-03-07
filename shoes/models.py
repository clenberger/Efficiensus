from django.db import models


class Shoe(models.Model):
    shoe_brand = models.CharField(max_length=75)
    shoe_owner = models.CharField(max_length=75)
    description = models.TextField(help_text="Write a desciption of your shoes!")
    created = models.DateTimeField(auto_now_add=True)    
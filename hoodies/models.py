from django.db import models

# Create your models here.
class Hoodie(models.Model):
    hoodie_brand = models.CharField(max_length=75)
    hoodie_owner = models.CharField(max_length=75)
    description = models.TextField(help_text="Write the desciption of your hoodie!")
    created = models.DateTimeField(auto_now_add=True)    
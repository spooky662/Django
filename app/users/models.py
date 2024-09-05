from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key = True)
    name = models.TextField(max_length = 255)
    phone = models.IntegerField()
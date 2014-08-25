from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    description = models.CharField(max_length=200)


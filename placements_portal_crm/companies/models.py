from django.db import models

# Create your models here.
class Csedata(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=2000,null=True)
    last_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.name
# class CseKnowmore(model.Model)

class Mechdata(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.name

class EEEdata(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.name

class Civildata(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.name


    
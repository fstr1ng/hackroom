from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

class Signature(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    example = models.TextField()
    extention = models.CharField(max_length=32)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    visible = models.BooleanField()
    deleted = models.BooleanField()

    def __str__(self):
        return self.name



class SubSig(models.Model):
    pass

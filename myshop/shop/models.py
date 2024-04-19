from django.db import models

class Shopdata(models.Model):
    item = models.CharField(max_length=255)
    count = models.IntegerField()
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item} - {self.size}"

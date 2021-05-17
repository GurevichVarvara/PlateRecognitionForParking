from django.db import models


class Plate(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    img_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.img_title


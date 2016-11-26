from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

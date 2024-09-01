from django.db import models

# Create your models here.


class To_do(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="gallery/")
    alt = models.CharField(max_length=255, default="Image Name")

    def __str__(self) -> str:
        return self.alt
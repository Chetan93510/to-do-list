from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Notifiction(models.Model):
    id = models.AutoField(primary_key=True)    
    content = models.TextField()

    def __str__(self):
        return self.content
    

@receiver(post_save, sender=Post)
def create_notification(sender, instance, **kwargs):
    if not instance.pk:
        Notifiction.objects.create(content=f"New Post Added '{instance.title}'")
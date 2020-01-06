from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyUser(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_site = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username

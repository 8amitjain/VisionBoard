from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
import os

class Vision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="vision_profile/",
        editable=True,
        help_text="Profile Picture",
        verbose_name="Profile Picture",
        default='default.jpg'
    )
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="400")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="400")

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img1 = Image.open(self.image.path)

        if img1.height > 1000 or img1.width > 1000:
            output_size = (1000, 1000)
            img1 = img1.resize(output_size)
            img1.save(self.image.path)

    def get_absolute_url(self):
        return reverse('vision-view-all', kwargs={'username': self.user})


class Photo(models.Model):
    file = models.ImageField(upload_to='vision_photos/', verbose_name='Photo')
    vision = models.ForeignKey(Vision, default=None, on_delete=models.CASCADE)

    def save(self):
        super().save()

        img = Image.open(self.file.path)

        if img.height > 500 or img.width > 333:
            output_size = (500, 333)
            img = img.resize(output_size)
            img.save(self.file.path)




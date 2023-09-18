from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='pages/media/images/')


class VideoModel(models.Model):
    video = models.FileField(upload_to='pages/media/videos/')

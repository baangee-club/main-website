from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from easy_thumbnails.files import get_thumbnailer
from PIL import Image


def resize_image(image):
    size = (500, 500)
    filename = str(image.path)
    new_image = Image.open(filename)
    new_image.thumbnail(size, Image.ANTIALIAS)
    new_image.save(filename)


class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to="gallery")
    uploading_time = models.DateTimeField(default=datetime.now, editable=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def image_tag(self):
        url = get_thumbnailer(self.image)["thumb"].url
        return f"<img width='150' src='{url}'>"

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        super(Photo, self).save()
        resize_image(self.image)


class Programme(models.Model):
    heading = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="programme", blank=True, null=True)
    image2 = models.ImageField(upload_to="programme", blank=True, null=True)
    image3 = models.ImageField(upload_to="programme", blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading


class Guest(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(Guest, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    creation_time = models.DateTimeField(default=datetime.now, editable=False)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=datetime.now)
    image1 = models.ImageField(upload_to="article", blank=True, null=True)
    image2 = models.ImageField(upload_to="article", blank=True, null=True)
    image3 = models.ImageField(upload_to="article", blank=True, null=True)

    def __unicode__(self):
        return self.title


class Soach(models.Model):
    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content


class Information(models.Model):
    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content


class ContactPerson(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="contact_persons")
    designation = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    mobile_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

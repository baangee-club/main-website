from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Album(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField()
	creation_time=models.DateTimeField(default=datetime.now,editable=False)	
	def __str__(self):
		return self.name

class Photo(models.Model):
	image=models.ImageField(upload_to="gallery")
	uploading_time=models.DateTimeField(default=datetime.now,editable=False)
	album=models.ForeignKey(Album)

	def image_tag(self):
		return '<img width="150" src="%s">' % self.image.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True
	
class Programme(models.Model):
	heading=models.CharField(max_length=70)
	description=models.TextField()
	image1=models.ImageField(upload_to='programme',blank=True,null=True)
	image2=models.ImageField(upload_to='programme',blank=True,null=True)
	image3=models.ImageField(upload_to='programme',blank=True,null=True)
	album=models.ForeignKey(Album,blank=True,null=True)
	
	def __str__(self):
		return self.heading

class Guest(models.Model):
	name=models.CharField(max_length=70)
	email=models.EmailField(unique=True)
	
	def __str__(self):
		return self.name
	
class Message(models.Model):
	author=models.ForeignKey(Guest)
	message=models.CharField(max_length=100)
	creation_time=models.DateTimeField(default=datetime.now,editable=False)


class Article(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	author=models.ForeignKey(User)
	creation_time=models.DateTimeField(default=datetime.now)
	image1=models.ImageField(upload_to='article',blank=True,null=True)
	image2=models.ImageField(upload_to='article',blank=True,null=True)
	image3=models.ImageField(upload_to='article',blank=True,null=True)
	

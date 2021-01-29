from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	full_name = models.CharField(max_length=60)
	image = models.ImageField(upload_to="static/user_pic")
	city = models.CharField(max_length=100)
	gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female')))
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(
		User, 
		on_delete=models.CASCADE,
		related_name='user'
		)

	def __str__(self):
		return self.full_name

class Project(models.Model):
	title = models.CharField(max_length=60)
	image = models.ImageField(upload_to="static/project_image")
	description = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	profile = models.ForeignKey(
		Profile, 
		on_delete=models.CASCADE,
		related_name='profile'
		)

	def __str__(self):
		return self.title
from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=100)
	bloggerimage=models.ImageField(upload_to="bloggerimg")
	name=models.CharField(max_length=20)
	date=models.DateTimeField(auto_now=False,auto_now_add=False)
	blog=models.CharField(max_length=1000)

	
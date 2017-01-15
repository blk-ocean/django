from django.db import models

# Create your models here.
class Lounge(models.Model):
	identifier=models.CharField(max_length=256,unique=True,default="null")
	name=models.CharField(max_length=256,unique=True)
	location=models.CharField(max_length=256,unique=False,default="null")
	text_summary=models.TextField(unique=False)
	address=models.TextField(unique=False)
	img1url=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.name


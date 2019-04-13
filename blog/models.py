from django.db import models

# Create your models here.

class BlogModel(models.Model):
	title = models.CharField(max_length = 200)
	publication_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')


	def summary(self):
		return self.body[:100]

	def publication_date_pretty(self):
		return self.publication_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title

from django.db import models

class Artist(models.Model):
	title = models.CharField(max_length=200)
	title_image = models.ImageField(upload_to='media/title_image', null=True)
	text = models.TextField()
	background_image = models.ImageField(upload_to='media/background-image',null=True)
	link = models.URLField(null=True, blank=True)

	def publish(self):
		self.save()

		def __str__(self):
			return self.title
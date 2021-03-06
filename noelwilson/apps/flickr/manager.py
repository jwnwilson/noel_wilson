from django.db import models

class PhotoManager(models.Manager):
	def published_photos(self):
		return self.model.objects.all().order_by('created')[8:]

from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=230)
	text = models.TextField()
	created_Date = models.DateTimeField(default=timezone.now)
	published_Date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_Date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
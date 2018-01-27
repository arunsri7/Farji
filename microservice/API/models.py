from __future__ import unicode_literals

from django.db import models

class NewsItem(models.Model):
	author = models.CharField(max_length=30)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=2000)
	source = models.CharField(max_length=200)

	def __str__(self):
		return "%d. %s" % (self.id, self.author)

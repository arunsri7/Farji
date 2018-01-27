from __future__ import unicode_literals

from django.db import models

class FakeNewsItem(models.Model):
	title = models.CharField(max_length=100)
	newsText = models.CharField(max_length=2000)
	sourceName = models.CharField(max_length=100, default="null")
	sourceURL = models.CharField(max_length=200, default="null")

	def __str__(self):
		return "%d. %s" % (self.id, self.title)

from rest_framework import serializers
from .models import FakeNewsItem

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = FakeNewsItem
		fields = '__all__'
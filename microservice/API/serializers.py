from rest_framework import serializers
from .models import FakeNewsItem

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = FakeNewsItem
		fields = ('title', 'newsText', 'sourceName', 'sourceURL')

# class ValidationSerializer(serializers.Serializer):
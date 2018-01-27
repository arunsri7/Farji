# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import FakeNewsItem
from .serializers import ReportSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView

from newsapi import NewsApiClient

# initilize the news API
newsapi = NewsApiClient(api_key='3111edae78f6492983bd0a6df945356e')

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def NewsItems(request):
    """Returns a JSON object, discribing the complete validation on the given news item"""

    if request.method == 'POST':
        # try:
            payload = request.POST['newsText'].replace(".", "").replace(" ", ", ")
            items = newsapi.get_everything(q=payload)
            return Response({
            	"aScore": items['totalResults'],
            	"newsText": request.POST['newsText'],
            	"sample": items["articles"][0]["source"]["name"],
            	"url": items["articles"][0]["url"],
            	"status": 200
            })
        # except KeyError:
            # return Response({"errorMessage": "required parameters are not met", "post": request.POST})
    return Response({"errorMessage": "Wrong request is being used"})

class ReportNews(CreateAPIView):
    queryset = FakeNewsItem.objects.all()
    serializer_class = ReportSerializer
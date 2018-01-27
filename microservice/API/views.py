# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import NewsItem
from .serializers import NewsItemSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from newsapi import NewsApiClient


# initilize the news API
newsapi = NewsApiClient(api_key='3111edae78f6492983bd0a6df945356e')

@api_view(['GET'])
def NewsItems(request):
    """Returns a JSON object, discribing the complete validation on the given news item"""
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    elif request.method == 'GET':
    	items = newsapi.get_everything(q="trump, modi, 2018, india, US, election")
    	return Response({"length": items})
    return Response({"message": "Hello, world!"})
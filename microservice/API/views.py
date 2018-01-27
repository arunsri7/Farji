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

sources = "crypto-coins-news,bbc-sport,google-news-au,rte,google-news-it,business-insider,google-news,hacker-news,the-sport-bible,recode,info-money,bleacher-report,financial-times,la-nacion,gruenderszene,bbc-news,four-four-two,la-gaceta,ynet,the-guardian-au,mtv-news-uk,google-news-fr,nhl-news,entertainment-weekly,wired-de,news-com-au,google-news-sa,news24,independent,rtl-nieuws,the-next-web,the-economist,google-news-ca,cbc-news,the-new-york-times,the-telegraph,sabq,nfl-news,espn-cric-info,fox-news,national-geographic,axios,vice-news,the-washington-post,reuters,ary-news,bloomberg,fox-sports,la-repubblica,espn,google-news-is,lequipe,business-insider-uk,google-news-ru,msnbc,google-news-in,google-news-uk,metro,techcrunch-cn,google-news-ar,aftenposten,nrk,wirtschafts-woche,cbs-news,xinhua-net,newsweek,liberation,goteborgs-posten,handelsblatt,the-guardian-uk,associated-press,talksport,mashable,rbc,rt,ansa,fortune,cnbc,al-jazeera-english,the-wall-street-journal,football-italia,buzzfeed,the-globe-and-mail,the-huffington-post,cnn-es,reddit-r-all,google-news-br,lenta,techradar,argaam,mirror,engadget,the-hill,wired,abc-news-au,il-sole-24-ore,nbc-news,ars-technica,politico,infobae,abc-news,cnn,blasting-news-br,svenska-dagbladet,the-times-of-india,medical-news-today,time,focus,usa-today,t3n,daily-mail,the-lad-bible,el-mundo,les-echos,new-york-magazine,le-monde,polygon,ign,new-scientist,mtv-news,the-hindu,spiegel-online,globo,marca,techcrunch,the-irish-times,next-big-future,bild,der-tagesspiegel,australian-financial-review,financial-post,the-verge,die-zeit,breitbart-news";

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def NewsItems(request):
    """Returns a JSON object, discribing the complete validation on the given news item"""

    if request.method == 'POST':
        # try:
            payload = request.POST['newsText'].replace(".", "").replace(" ", ", ")
            
            items = newsapi.get_everything(
            	q=payload,
            	sources=sources
            )

            aScore = items['totalResults']
            sources = [{
            	"name": item["source"]["name"], 
            	"url": item["url"],
            	"description": item["description"]
            } for item in items["articles"]]

            return Response({
            	"aScore": aScore,
            	"newsText": request.POST['newsText'],
            	"sources": sources,
            	"status": 200,
            	"res": items
            })
        # except KeyError:
            # return Response({"errorMessage": "required parameters are not met", "post": request.POST})
    return Response({"errorMessage": "Wrong request is being used"})

class ReportNews(CreateAPIView):
    queryset = FakeNewsItem.objects.all()
    serializer_class = ReportSerializer
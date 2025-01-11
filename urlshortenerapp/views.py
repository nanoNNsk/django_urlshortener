from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UrlModel
from django.shortcuts import redirect

# Create your views here.
@api_view(['POST'])
def createShortUrl(request):
    longUrl = request.data['longUrl']
    urlModel = UrlModel(longUrl=longUrl)
    urlModel.save()
    shorturl = urlModel.shortUrl
    return Response({
        'shortUrl':shorturl
    })

@api_view(['GET','POST'])
def redirectToLongUrl(request,shortUrl):
    urlModel = UrlModel.objects.get(shortUrl=shortUrl)
    return redirect(urlModel.longUrl)
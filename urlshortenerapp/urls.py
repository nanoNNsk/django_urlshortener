from django.urls import path,include
from .views import createShortUrl,redirectToLongUrl

urlpatterns = [
    path('api/create',createShortUrl),
    path('<str:shortUrl>',redirectToLongUrl)
]
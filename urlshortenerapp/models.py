from django.db import models
from hashids import Hashids # type: ignore

# Create your models here.
def generatefromid(id):
    return Hashids(salt='urlshortenerapp',min_length=5).encode(id)
    

class UrlModel(models.Model):
    longUrl = models.URLField()
    shortUrl = models.CharField(max_length=1000)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.shortUrl = generatefromid(self.id)
        super().save(*args,**kwargs)
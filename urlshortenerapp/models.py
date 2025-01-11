from django.db import models

# Create your models here.
def generateramdomsrting(min_length):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(min_length))

class UrlModel(models.Model):
    longUrl = models.URLField()
    shortUrl = models.CharField(max_length=1000)

    def save(self,*args,**kwargs):
        self.shortUrl = generateramdomsrting(min_length=6)
        super().save(*args,**kwargs)
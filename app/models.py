from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail



class Restaurant(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    restimage = ProcessedImageField(blank=True,
            processors=[Thumbnail(350, 350)],
            upload_to='app/restimage/%Y/%m/%d',
            format='JPEG',
            options={'quality': 80})
    restname = models.CharField(max_length=50)
    restsite = models.CharField(max_length=200)

    def __str__(self):
        return self.restname

    def get_absolute_url(self):
        return reverse('app:rest_index')

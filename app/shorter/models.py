from django.db import models


class Url(models.Model):
    redirect_url = models.URLField()
    key = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.key

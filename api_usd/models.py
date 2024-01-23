from django.db import models


class Currency(models.Model):
    value = models.FloatField()
    request_date = models.DateTimeField(auto_now_add=True)

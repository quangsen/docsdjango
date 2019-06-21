from django.db import models
import datetime
from django.contrib.contenttypes.fields import GenericRelation

class Category(models.Model):
    name = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField(default=1)


class Metric(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    categroy = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    position = models.PositiveSmallIntegerField(default=1)
    data = GenericRelation('Datum')
    show_on_dashboard = models.BooleanField(default=True)
    show_sparkline = models.BooleanField(default=True)
    unit = models.CharField(max_length=100)
    unit_plural = models.CharField(max_length=100)

class TracTicketMetric(Metric):
    query = models.TextField()
        

class RSSFeedMetric(Metric):
    feed_url = models.URLField(max_length=1000)
    link_url = models.URLField(max_length=1000)


class GithubItemCountMetric(Metric):
    api_url = models.URLField(max_length=1000)
    link_url = models.URLField(max_length=1000)

class Datum(models.Model):
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    measurement = models.BigIntegerField()

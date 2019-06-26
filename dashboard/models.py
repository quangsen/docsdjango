from django.db import models
import datetime
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.models import ContentType

METRIC_PERIOD_INSTANT = 'instant'
METRIC_PERIOD_DAILY = 'daily'
METRIC_PERIOD_WEEKLY = 'weekly'
METRIC_PERIOD_CHOICES = (
    (METRIC_PERIOD_INSTANT, 'Instant'),
    (METRIC_PERIOD_DAILY, 'Daily'),
    (METRIC_PERIOD_WEEKLY, 'Weekly'),
)

class Category(models.Model):
    name = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField(default=1)


class Metric(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    position = models.PositiveSmallIntegerField(default=1)
    data = GenericRelation('Datum')
    show_on_dashboard = models.BooleanField(default=True)
    show_sparkline = models.BooleanField(default=True)
    period = models.CharField(max_length=15, choices=METRIC_PERIOD_CHOICES, default=METRIC_PERIOD_INSTANT)
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

class JenkinsFailuresMetric(Metric):
    jenkins_root_url = models.URLField(
        verbose_name='Jenkins instance root URL',
        max_length=1000,
        help_text='E.g. http://ci.djangoproject.com/',
    )
    build_name = models.CharField(
        max_length=100,
        help_text='E.g. Django Python3',
    )
    is_success_cnt = models.BooleanField(
        default=False,
        verbose_name='Should the metric be a value representing success ratio?',
        help_text='E.g. if there are 50 tests of which 30 are failing the value of this metric '
                  'will be 20 (or 40%.)',
    )
    is_percentage = models.BooleanField(
        default=False,
        verbose_name='Should the metric be a percentage value?',
        help_text='E.g. if there are 50 tests of which 30 are failing the value of this metric '
                  'will be 60%.',
    )

class Datum(models.Model):
    metric = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, related_name='+', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    measurement = models.BigIntegerField()

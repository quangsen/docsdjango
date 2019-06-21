# Generated by Django 2.1.8 on 2019-06-21 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GithubItemCountMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.Metric')),
                ('api_url', models.URLField(max_length=1000)),
                ('link_url', models.URLField(max_length=1000)),
            ],
            bases=('dashboard.metric',),
        ),
        migrations.CreateModel(
            name='RSSFeedMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.Metric')),
                ('feed_url', models.URLField(max_length=1000)),
                ('link_url', models.URLField(max_length=1000)),
            ],
            bases=('dashboard.metric',),
        ),
        migrations.CreateModel(
            name='TracTicketMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.Metric')),
                ('query', models.TextField()),
            ],
            bases=('dashboard.metric',),
        ),
    ]
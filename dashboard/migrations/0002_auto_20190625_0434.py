# Generated by Django 2.1.7 on 2019-06-25 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='categroy',
            new_name='category',
        ),
    ]

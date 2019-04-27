# Generated by Django 2.0.13 on 2019-04-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruck',
            name='truckdate',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodtruck',
            name='trucktime',
            field=models.CharField(default=0.38461538461538464, max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.13 on 2019-05-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_award_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imagelink',
            field=models.CharField(default='', max_length=2000),
        ),
    ]

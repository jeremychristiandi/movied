# Generated by Django 4.2.8 on 2023-12-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

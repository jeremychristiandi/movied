# Generated by Django 4.2.8 on 2023-12-22 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_actor_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starring',
            name='actor',
        ),
        migrations.AddField(
            model_name='starring',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='movies.actor'),
        ),
    ]

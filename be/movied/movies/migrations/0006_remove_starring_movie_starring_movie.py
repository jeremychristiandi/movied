# Generated by Django 4.2.8 on 2023-12-14 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_starring_movie_starring_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starring',
            name='movie',
        ),
        migrations.AddField(
            model_name='starring',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.movie'),
        ),
    ]

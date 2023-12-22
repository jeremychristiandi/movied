# Generated by Django 4.2.8 on 2023-12-14 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_actor_movie_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(to='movies.movie'),
        ),
        migrations.CreateModel(
            name='Starring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ManyToManyField(to='movies.actor')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.movie')),
            ],
        ),
    ]

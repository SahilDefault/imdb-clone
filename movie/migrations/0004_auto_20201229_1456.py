# Generated by Django 3.1.4 on 2020-12-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANACE')], max_length=10),
        ),
    ]

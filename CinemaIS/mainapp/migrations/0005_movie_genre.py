# Generated by Django 5.1.1 on 2024-10-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_movie_desc_img_alter_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='non-genre', max_length=30),
        ),
    ]

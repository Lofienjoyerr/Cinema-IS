# Generated by Django 5.1.1 on 2024-10-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='format',
            field=models.CharField(help_text='2D or 3D', max_length=2),
        ),
    ]
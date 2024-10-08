# Generated by Django 5.1.1 on 2024-10-04 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_movie_id_session_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie')),
            ],
        ),
        migrations.CreateModel(
            name='FunMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie')),
            ],
        ),
        migrations.CreateModel(
            name='SadMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie')),
            ],
        ),
        migrations.CreateModel(
            name='TopMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie')),
            ],
        ),
    ]

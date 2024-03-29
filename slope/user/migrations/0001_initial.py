# Generated by Django 4.1.5 on 2023-02-02 18:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120, null=True)),
                ('lastname', models.CharField(max_length=120, null=True)),
                ('email', models.CharField(max_length=120, null=True, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('account_type', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue'), ('Consumer', 'Consumer')], max_length=120, null=True)),
                ('brand_name', models.CharField(max_length=120, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('city', models.CharField(max_length=120, null=True)),
                ('mobile_number', models.CharField(max_length=120, null=True)),
                ('account_types_all', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50, null=True), default=list, size=None)),
                ('music_genres_all', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120, null=True), default=list, size=None)),
                ('profile_picture', models.CharField(max_length=1024, null=True)),
                ('website_link', models.CharField(max_length=120, null=True)),
                ('social_media_link', models.CharField(max_length=120, null=True)),
                ('spotify_link', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]

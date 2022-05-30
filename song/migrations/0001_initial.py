# Generated by Django 4.0.4 on 2022-05-30 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('num_stars', models.IntegerField()),
                ('release_date', models.DateField()),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('num_stars', models.IntegerField()),
                ('album', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='song.album')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
    ]

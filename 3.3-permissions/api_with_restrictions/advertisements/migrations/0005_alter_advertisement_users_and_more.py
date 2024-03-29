# Generated by Django 5.0.2 on 2024-02-16 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_rename_favoriteadvertisement_favorite_advertisements'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='users',
            field=models.ManyToManyField(related_name='my_advertisements', through='advertisements.Favorite_advertisements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorite_advertisements',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='advertisements.advertisement'),
        ),
        migrations.AlterField(
            model_name='favorite_advertisements',
            name='favorite',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='favorite_advertisements',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to=settings.AUTH_USER_MODEL),
        ),
    ]

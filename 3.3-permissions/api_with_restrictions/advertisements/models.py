from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = "DRAFT", "Черновик"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Favorite_advertisements',
    related_name = 'my_advertisements'
    )

class Favorite_advertisements(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='positions'
    )
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='positions'
    )
    favorite = models.BooleanField(default=True)


from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель локации
class Locations(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


# Модель пользователя
class User(AbstractUser):
    MEMBER = "Пользователь"
    MODERATOR = "Модератор"
    ADMIN = "Администратор"
    ROLES = [
        (MEMBER, MEMBER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    ]

    role = models.CharField(max_length=13, choices=ROLES, default=MEMBER)
    age = models.SmallIntegerField(null=True)
    location_id = models.ManyToManyField(Locations, blank=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username

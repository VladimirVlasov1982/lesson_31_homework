from django.db import models
from users.models import User


class Categories(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=300)

    objects = models.Manager()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ads(models.Model):
    """Модель объявления"""
    name = models.CharField(max_length=200)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ads", null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to="pictures", null=True, blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    """Модель подборки"""
    name = models.CharField(max_length=150, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    items = models.ManyToManyField(Ads)

    objects = models.Manager()

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name

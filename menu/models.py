from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        default=""
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена:")
    weight = models.CharField(max_length=50, verbose_name="Вес:")
    image = models.ImageField(upload_to='dishes/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.name
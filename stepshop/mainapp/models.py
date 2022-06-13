from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=128,
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    def __str__(self):
        return self.name or f'Категория с id - {self.pk}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name='изображение',
    )

    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=128,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='цена',
        max_digits=9,
        decimal_places=2,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    crated_at = models.DateTimeField(
        auto_now_add=True,
    )

    update_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name or f'Продукт с id - {self.pk}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

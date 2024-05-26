from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image_preview = models.ImageField(upload_to='catalog/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE,
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания (записи в БД)')
    updated_ad = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения (записи в БД)')


    def __str__(self):
        return f'{self.product_name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category']


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

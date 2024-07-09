from django.db import models, connection

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='catalog/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE,
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания (записи в БД)')
    updated_ad = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения (записи в БД)')

    view_counter = models.PositiveIntegerField(
        verbose_name='Количество просмотров',
        help_text='Количество просмотров данного товара',
        default=0
    )
    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца продукта', blank=True, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(blank=True, null=True, default=False, verbose_name='Публикация')

    def __str__(self):
        return f'{self.product_name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = (
            "price",
            "category",
            "created_at",
            "updated_ad",
        )
        permissions = [
            ("can_edit", "Can edit category"),
            ("can_edit_description", "Can edit description"),
            ('can_edit_is_published', 'Can edit is_published'),
        ]


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.category_name

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
            #
            # cursor.execute(f"ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")
            # cursor.execute(f"ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='product_versions', on_delete=models.SET_NULL, **NULLABLE, verbose_name='продукт')
    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.current_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

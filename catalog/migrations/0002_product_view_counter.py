# Generated by Django 5.0.6 on 2024-06-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Количество просмотров данного товара', verbose_name='Количество просмотров'),
        ),
    ]

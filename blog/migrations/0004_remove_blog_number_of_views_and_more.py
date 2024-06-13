# Generated by Django 5.0.6 on 2024-06-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blogs_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='number_of_views',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='publication_sing',
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AddField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog/preview', verbose_name='Превью (изображение)'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesForFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Названия категорий')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория цветов',
                'verbose_name_plural': 'Категории цветов',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.CreateModel(
            name='CategoriesForOthers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Прочее')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория прочего',
                'verbose_name_plural': 'Категории прочего',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='others/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flowers.categoriesforothers')),
            ],
            options={
                'verbose_name': 'Прочее',
                'verbose_name_plural': 'Прочее',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='flowers/%Y/%m/%d/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('is_published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flowers.categoriesforflowers')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
                'ordering': ['id', 'title'],
            },
        ),
    ]

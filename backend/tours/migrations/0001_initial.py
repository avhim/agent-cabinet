# Generated by Django 5.0.6 on 2024-05-10 09:08

import django.db.models.deletion
import tours.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tours/categoty')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тип тура',
                'verbose_name_plural': 'Типы туров',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CountryTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Отображать')),
                ('title', models.CharField(max_length=128, verbose_name='Название тура')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на тур')),
                ('seo_keywords', models.TextField(blank=True, null=True, verbose_name='SEO слова')),
                ('seo_description', models.TextField(blank=True, null=True, verbose_name='SEO описание')),
                ('img', models.ImageField(upload_to=tours.models.tours_img_upload)),
                ('first_title', models.TextField(blank=True, null=True, verbose_name='Заголовок на изображении')),
                ('second_title', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Старая цена')),
                ('currency', models.CharField(choices=[('$', '$'), ('€', '€'), ('BYN', 'BYN'), ('₽', '₽')], default='BYN', max_length=10, verbose_name='валюта')),
                ('service_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Туруслуга взрослый')),
                ('service_price_child', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Туруслуга детский')),
                ('comission', models.FloatField(blank=True, default=10, null=True, verbose_name='Комиссия')),
                ('route', models.TextField(blank=True, null=True, verbose_name='Маршрут')),
                ('num_days', models.IntegerField(default=1, verbose_name='Количество дней')),
                ('night_transfer', models.IntegerField(default=0, verbose_name='Ночных перездов')),
                ('description_tour', models.TextField(blank=True, null=True, verbose_name='описание тура')),
                ('included', models.TextField(blank=True, null=True, verbose_name='Включено в стоимость')),
                ('not_included', models.TextField(blank=True, null=True, verbose_name='Дополнительно оплачивается')),
                ('count_views', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ManyToManyField(to='tours.categorytour', verbose_name='тип тура')),
                ('country', models.ManyToManyField(to='tours.countrytour')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='TourDayQuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активная дата')),
                ('tour_date', models.DateField(null=True, verbose_name='Дата тура')),
                ('total_quotas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Всего мест')),
                ('sold_quotas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Проданные места')),
                ('price_adult', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена взрослый')),
                ('price_child', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена детский')),
                ('tour', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tour_day_quota', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Дата-Квота',
                'verbose_name_plural': 'Даты-Квоты',
                'ordering': ['tour_date'],
            },
        ),
        migrations.CreateModel(
            name='TourDescriptionDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('day', models.CharField(default='День 1', max_length=12)),
                ('description', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tour_description_day', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Описание дня',
                'verbose_name_plural': 'Описание дней',
            },
        ),
    ]

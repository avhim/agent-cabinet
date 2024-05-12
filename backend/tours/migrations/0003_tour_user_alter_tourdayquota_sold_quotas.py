# Generated by Django 5.0.6 on 2024-05-10 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_tour_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tourdayquota',
            name='sold_quotas',
            field=models.PositiveIntegerField(default=0, verbose_name='Проданные места'),
        ),
    ]
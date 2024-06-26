# Generated by Django 5.0.6 on 2024-05-27 11:17

import django.db.models.deletion
import filer.fields.image
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_tour_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='img',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tour_image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='tour',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tour_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]

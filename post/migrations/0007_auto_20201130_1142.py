# Generated by Django 3.1.3 on 2020-11-30 06:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20201130_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator('png', 'jpg', 'jpeg')]),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-28 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_relationship'),
        ('post', '0002_auto_20201128_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='user_profile.Profile'),
        ),
    ]

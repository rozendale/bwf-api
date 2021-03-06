# Generated by Django 4.0.2 on 2022-03-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.BooleanField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]

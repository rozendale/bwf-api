# Generated by Django 4.0.2 on 2022-03-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_userprofile_bio_userprofile_is_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]

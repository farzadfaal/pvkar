# Generated by Django 4.0.2 on 2022-03-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس صفحه\u200cی اینستاگرام'),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس صفحه\u200cی تلگرام'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_certificate_options_alter_profile_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='work_experience',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='سابقه کار مفید'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-26 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_emailaddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'verbose_name': 'شماره تلفن', 'verbose_name_plural': 'شماره تلفن\u200cها'},
        ),
    ]
# Generated by Django 4.0.2 on 2022-04-07 15:20

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=6, lowercase=True, primary_key=True, serialize=False, unique=True),
        ),
    ]

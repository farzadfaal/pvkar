# Generated by Django 4.0.2 on 2022-03-26 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_rename_description_proposal_general_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='finance',
            new_name='financcial_description',
        ),
    ]
# Generated by Django 4.0.5 on 2022-09-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_stockgroupcreation_comp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockgroupcreation',
            old_name='comp',
            new_name='company',
        ),
    ]

# Generated by Django 4.0.4 on 2022-09-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0048_journal_credit_journal_debit_journal_particularsto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency_alt',
            name='buyvorate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='currency_alt',
            name='selvorate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

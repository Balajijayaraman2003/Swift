# Generated by Django 5.1.4 on 2025-06-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance_Management', '0002_rename_fund_expence_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalAmount', models.FloatField(default=0)),
            ],
        ),
    ]

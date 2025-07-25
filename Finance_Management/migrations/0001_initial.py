# Generated by Django 5.1.4 on 2025-06-28 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Events', '0002_event_head_event_sub_heads_alter_event_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_provider', models.CharField(max_length=200)),
                ('regno', models.CharField(blank=True, help_text='requrired if the provider is student', max_length=200, null=True)),
                ('cls', models.CharField(blank=True, help_text='requrired if the provider is student', max_length=200, null=True)),
                ('type', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund', models.FloatField()),
                ('date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2025-06-29 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_quardinators_department'),
        ('Events', '0002_event_head_event_sub_heads_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='head',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_head', to='Authentication.swifters'),
        ),
    ]

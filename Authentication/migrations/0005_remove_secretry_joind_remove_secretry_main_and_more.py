# Generated by Django 5.1.4 on 2025-06-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_secretry_joind_secretry_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretry',
            name='joind',
        ),
        migrations.RemoveField(
            model_name='secretry',
            name='main',
        ),
        migrations.AddField(
            model_name='secretry',
            name='type',
            field=models.CharField(blank=True, choices=[('Chief', 'Chief'), ('Chief-Joind', 'Chief-Joid'), ('Joind', 'Joind')], max_length=200, null=True),
        ),
    ]

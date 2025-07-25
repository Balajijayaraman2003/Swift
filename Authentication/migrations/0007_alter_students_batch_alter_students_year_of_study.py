# Generated by Django 5.1.4 on 2025-06-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0006_students_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='batch',
            field=models.CharField(help_text='Example : 2021-2024', max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='year_of_study',
            field=models.CharField(choices=[('I-Year', 'I-Year'), ('II-Year', 'II-Year'), ('III-Year', 'III-Year')], default=1, max_length=200),
        ),
    ]

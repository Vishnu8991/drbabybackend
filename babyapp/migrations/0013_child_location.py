# Generated by Django 4.2.9 on 2024-01-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyapp', '0012_vaccineprograms'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='Location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

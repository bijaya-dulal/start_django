# Generated by Django 4.2.7 on 2024-01-10 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='section',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

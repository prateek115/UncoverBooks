# Generated by Django 3.0.4 on 2021-06-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncoverBooks', '0005_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.AddField(
            model_name='orders',
            name='address1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='orders',
            name='address2',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

# Generated by Django 3.0.4 on 2021-07-06 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncoverBooks', '0013_auto_20210706_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Index',
            field=models.Field(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(default='', max_length=200000),
        ),
    ]

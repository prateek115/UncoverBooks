# Generated by Django 3.0.4 on 2021-07-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncoverBooks', '0010_productcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Index',
            field=models.IntegerField(default=0),
        ),
    ]

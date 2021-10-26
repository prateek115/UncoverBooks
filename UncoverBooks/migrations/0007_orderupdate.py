# Generated by Django 3.0.4 on 2021-06-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncoverBooks', '0006_auto_20210613_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('update_desc', models.CharField(max_length=4000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

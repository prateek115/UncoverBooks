# Generated by Django 3.0.4 on 2021-06-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncoverBooks', '0002_auto_20210526_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]

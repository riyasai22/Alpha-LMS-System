# Generated by Django 2.2 on 2022-06-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20220614_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='returned',
            name='fine',
            field=models.IntegerField(default=0),
        ),
    ]

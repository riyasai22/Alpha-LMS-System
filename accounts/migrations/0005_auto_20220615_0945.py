# Generated by Django 2.2 on 2022-06-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_studentprofile_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='date_of_joining',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
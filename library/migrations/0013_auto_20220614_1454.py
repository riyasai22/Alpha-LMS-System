# Generated by Django 2.2 on 2022-06-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_renewrequests_renew_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renewrequests',
            name='renew_count',
        ),
        migrations.AddField(
            model_name='issue',
            name='renew_count',
            field=models.IntegerField(default=2),
        ),
    ]
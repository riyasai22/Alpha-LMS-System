# Generated by Django 2.2 on 2022-06-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_returned_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('info', 'info'), ('warning', 'warning'), ('approval', 'approval')], default='approval', max_length=20),
        ),
    ]

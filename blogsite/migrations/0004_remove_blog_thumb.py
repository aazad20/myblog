# Generated by Django 2.2.3 on 2022-12-16 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0003_auto_20221213_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumb',
        ),
    ]

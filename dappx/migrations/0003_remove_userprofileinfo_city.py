# Generated by Django 2.1.1 on 2019-05-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0002_auto_20190510_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='city',
        ),
    ]

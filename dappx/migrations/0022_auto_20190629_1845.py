# Generated by Django 2.2.1 on 2019-06-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0021_auto_20190629_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Fee_Payment',
        ),
        migrations.AlterField(
            model_name='tutorquestion',
            name='Upload_certificate',
            field=models.ImageField(blank=True, upload_to='Upload_certificate'),
        ),
    ]

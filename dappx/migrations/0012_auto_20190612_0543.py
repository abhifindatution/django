# Generated by Django 2.1.1 on 2019-06-12 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0011_auto_20190607_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutionpointregister',
            old_name='Fee_for_courses',
            new_name='Subjects_you_teach',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Give_us_a_short_description_about_yourself',
            new_name='Preferred_Tutor',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Prefferd_Tutor',
            new_name='Preferred_time',
        ),
        migrations.RemoveField(
            model_name='tutionpointregister',
            name='Subjects_you_wish_to_teach',
        ),
        migrations.RemoveField(
            model_name='tutionpointregister',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Prefferd_time',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='your_best_subject',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='your_worst_subject',
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-28 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newproject', '0008_rename_user_userblog_user_id_remove_profile_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
    ]
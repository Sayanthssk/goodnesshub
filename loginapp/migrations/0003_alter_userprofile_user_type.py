# Generated by Django 5.1.3 on 2024-11-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('RESTAURANT', 'Restaurant'), ('CAMP', 'Camp'), ('ADMIN', 'Admin'), ('USER', 'User')], max_length=20),
        ),
    ]

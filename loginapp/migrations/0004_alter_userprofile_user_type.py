# Generated by Django 5.1.3 on 2024-11-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User'), ('CAMP', 'Camp'), ('RESTAURANT', 'Restaurant')], max_length=20),
        ),
    ]

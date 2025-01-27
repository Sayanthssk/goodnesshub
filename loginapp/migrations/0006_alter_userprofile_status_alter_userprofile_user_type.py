# Generated by Django 5.1.3 on 2024-11-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], default='DEACTIVE', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('RESTAURANT', 'Restaurant'), ('ADMIN', 'Admin'), ('USER', 'User'), ('CAMP', 'Camp')], max_length=20),
        ),
    ]

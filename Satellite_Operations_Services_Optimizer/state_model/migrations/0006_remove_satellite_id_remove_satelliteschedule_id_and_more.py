# Generated by Django 4.1.5 on 2023-10-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state_model', '0005_rename_satellitescheduleid_groundstationrequest_satelliteid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='id',
        ),
        migrations.RemoveField(
            model_name='satelliteschedule',
            name='id',
        ),
        migrations.AlterField(
            model_name='satellite',
            name='satelliteId',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='satelliteschedule',
            name='scheduleID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]

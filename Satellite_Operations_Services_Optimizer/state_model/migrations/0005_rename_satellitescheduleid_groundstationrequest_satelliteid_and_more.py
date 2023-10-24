# Generated by Django 4.1.12 on 2023-10-23 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state_model', '0004_alter_downlinktask_schedule_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groundstationrequest',
            old_name='satelliteScheduleId',
            new_name='satelliteId',
        ),
        migrations.RemoveField(
            model_name='groundstationrequest',
            name='satellite',
        ),
        migrations.RemoveField(
            model_name='groundstationrequest',
            name='stationName',
        ),
        migrations.AddField(
            model_name='groundstationrequest',
            name='groundStation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ground_station_requests', to='state_model.groundstation'),
        ),
        migrations.AddField(
            model_name='groundstationrequest',
            name='requestId',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='outage',
            name='outageId',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='groundstation',
            name='stationName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
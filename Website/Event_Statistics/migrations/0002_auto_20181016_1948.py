# Generated by Django 2.1.1 on 2018-10-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_Statistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfBennies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfFreshman',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfJonnies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfJunior',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfLocal',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfOutOfState',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfSenior',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event_statistics',
            name='numberOfSophomore',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

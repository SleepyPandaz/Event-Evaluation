# Generated by Django 2.1.1 on 2018-10-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='ident',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Name'),
        ),
    ]
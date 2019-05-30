# Generated by Django 2.2 on 2019-05-30 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_length', models.IntegerField(choices=[('10', '10'), ('100', '100'), ('1000', '1000'), ('10000', '10000')])),
                ('unique_keys', models.BooleanField()),
                ('bubble', models.FloatField()),
                ('select', models.FloatField()),
                ('merge', models.FloatField()),
                ('heap', models.FloatField()),
                ('quick', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AverageTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_number', models.IntegerField(default=0)),
                ('avg_bubble', models.FloatField(default=0)),
                ('avg_select', models.FloatField(default=0)),
                ('avg_merge', models.FloatField(default=0)),
                ('avg_heap', models.FloatField(default=0)),
                ('avg_quick', models.FloatField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test_Sorting.TestInstance')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-05-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_Sorting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinstance',
            name='bubble',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='heap',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='merge',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='quick',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='select',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='unique_keys',
            field=models.BooleanField(default=True),
        ),
    ]

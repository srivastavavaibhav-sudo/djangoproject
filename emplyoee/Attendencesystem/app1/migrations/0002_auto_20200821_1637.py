# Generated by Django 3.1 on 2020-08-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='employee',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

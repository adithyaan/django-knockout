# Generated by Django 2.1.1 on 2020-09-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0011_auto_20200911_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

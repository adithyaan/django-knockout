# Generated by Django 2.1.1 on 2020-10-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0012_auto_20200911_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='name',
            field=models.CharField(max_length=222),
        ),
    ]
# Generated by Django 2.1.1 on 2020-09-11 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0010_auto_20200910_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='fixture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='fixture.Fixture'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='left_matches', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='right_matches', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches_won', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='fixture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='players', to='fixture.Fixture'),
        ),
    ]

# Generated by Django 2.1.1 on 2020-09-10 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0009_auto_20171124_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='fixture.Fixture'),
        ),
        migrations.AlterField(
            model_name='match',
            name='left_previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='left_next_match', to='fixture.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='left_matches', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='right_matches', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='right_previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='right_next_match', to='fixture.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches_won', to='fixture.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='players', to='fixture.Fixture'),
        ),
    ]

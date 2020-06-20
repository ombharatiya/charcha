# Generated by Django 3.0.7 on 2020-06-17 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200618_0024'),
        ('discussions', '0012_auto_20200615_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='teams.Team'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

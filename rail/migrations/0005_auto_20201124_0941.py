# Generated by Django 3.0.8 on 2020-11-24 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0004_auto_20201123_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berthNumber', models.IntegerField()),
                ('coachType', models.CharField(choices=[('SL', 'Sleeper'), ('AC', 'AC')], max_length=2)),
                ('berthType', models.CharField(choices=[('LB', 'LB'), ('UB', 'UB'), ('MB', 'MB'), ('SL', 'SL'), ('SU', 'SU')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachType', models.CharField(choices=[('SL', 'Sleeper'), ('AC', 'AC')], max_length=2)),
                ('coachNumber', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='releasedtrain',
            old_name='AcNumber',
            new_name='currAC',
        ),
        migrations.RenameField(
            model_name='releasedtrain',
            old_name='SlNumber',
            new_name='currSL',
        ),
        migrations.AddField(
            model_name='releasedtrain',
            name='maxAC',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasedtrain',
            name='maxSL',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rail.Berth')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rail.Coach')),
            ],
        ),
        migrations.AddField(
            model_name='coach',
            name='releasedTrain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rail.ReleasedTrain'),
        ),
    ]

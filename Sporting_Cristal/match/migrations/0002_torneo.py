# Generated by Django 2.0.7 on 2018-07-25 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=40)),
                ('referee', models.CharField(max_length=40)),
                ('local_goals', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('alineaciones', models.CharField(max_length=100)),
                ('city_reference_a', models.CharField(max_length=100)),
                ('city_reference_b', models.CharField(max_length=100)),
                ('heatmap', models.CharField(max_length=100)),
                ('id_opta', models.IntegerField()),
                ('image_streaming', models.CharField(max_length=100)),
                ('minute', models.FloatField()),
                ('slug', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('time', models.TimeField()),
                ('timestamp', models.FloatField()),
                ('visit_goals', models.IntegerField()),
                ('weather', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2021-04-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_covid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('updated', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('countryInfo', models.CharField(max_length=100)),
                ('cases', models.CharField(max_length=100)),
                ('todayCases', models.CharField(max_length=100)),
                ('deaths', models.CharField(max_length=100)),
                ('todayDeaths', models.CharField(max_length=100)),
                ('recovered', models.CharField(max_length=100)),
                ('todayRecovered', models.CharField(max_length=100)),
                ('active', models.CharField(max_length=100)),
                ('critical', models.CharField(max_length=100)),
                ('casesPerOneMillion', models.CharField(max_length=100)),
                ('deathsPerOneMillion', models.CharField(max_length=100)),
                ('tests', models.CharField(max_length=100)),
                ('testsPerOneMillion', models.CharField(max_length=100)),
                ('population', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('oneCasePerPeople', models.CharField(max_length=100)),
                ('oneDeathPerPeople', models.CharField(max_length=100)),
                ('activePerOneMillion', models.CharField(max_length=100)),
                ('recoveredPerOneMillion', models.CharField(max_length=100)),
                ('criticalPerOneMillion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'api_covid_data',
            },
        ),
        migrations.AlterField(
            model_name='todo',
            name='Country',
            field=models.CharField(db_column='Country,Other', default='country', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.IntegerField(default=1),
        ),
    ]
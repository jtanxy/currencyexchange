# Generated by Django 4.2.7 on 2023-11-08 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('source_currency', models.CharField(max_length=50)),
                ('target_currency', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DailyRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('high', models.DecimalField(decimal_places=4, max_digits=11)),
                ('low', models.DecimalField(decimal_places=4, max_digits=11)),
                ('close', models.DecimalField(decimal_places=4, max_digits=11)),
                ('last_updated', models.DateField()),
                ('currency_pairs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forex.currencypairs')),
            ],
        ),
    ]

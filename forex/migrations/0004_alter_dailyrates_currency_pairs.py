# Generated by Django 4.2.7 on 2023-11-10 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0003_alter_currencypairs_symbol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrates',
            name='currency_pairs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forex.currencypairs'),
        ),
    ]

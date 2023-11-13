# Generated by Django 4.2.7 on 2023-11-10 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencypairs',
            name='target_currency',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dailyrates',
            name='currency_pairs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_pairs_symbol', to='forex.currencypairs'),
        ),
    ]
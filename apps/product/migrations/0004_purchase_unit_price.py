# Generated by Django 4.2.4 on 2024-03-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_purchase_weekly_control_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=8),
            preserve_default=False,
        ),
    ]

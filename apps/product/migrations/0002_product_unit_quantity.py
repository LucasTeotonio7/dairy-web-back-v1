# Generated by Django 4.2.4 on 2023-09-22 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
        ),
    ]

# Generated by Django 4.2.4 on 2024-07-25 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-is_active', '-last_login'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]

# Generated by Django 4.0.2 on 2023-03-28 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_driver_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
    ]
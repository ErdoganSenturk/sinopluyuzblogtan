# Generated by Django 4.2.4 on 2023-08-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinoplu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sinopluyuz',
            options={},
        ),
        migrations.AlterField(
            model_name='sinopluyuz',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

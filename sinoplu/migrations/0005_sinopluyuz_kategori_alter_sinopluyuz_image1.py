# Generated by Django 4.2.4 on 2023-10-05 19:13

from django.db import migrations, models
import sinoplu.models


class Migration(migrations.Migration):

    dependencies = [
        ('sinoplu', '0004_alter_sinopluyuz_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinopluyuz',
            name='kategori',
            field=models.CharField(choices=[('eğitim', 'Eğitim'), ('sağlık', 'Sağlık'), ('inşaat', 'İnşaat'), ('gıda', 'Gıda'), ('ulaşım', 'Ulaşım')], default='Eğitim', max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='sinopluyuz',
            name='image1',
            field=models.ImageField(default='sinoplu.jpg', upload_to=sinoplu.models.user_directory_path),
        ),
    ]

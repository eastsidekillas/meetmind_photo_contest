# Generated by Django 4.2.5 on 2023-11-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_alter_category_options_alter_photo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='uploads/photos/', verbose_name='Изображение'),
        ),
    ]

# Generated by Django 4.2.3 on 2024-09-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshopthrift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]

# Generated by Django 3.1.13 on 2023-08-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]

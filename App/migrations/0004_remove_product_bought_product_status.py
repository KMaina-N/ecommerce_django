# Generated by Django 4.1.4 on 2022-12-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_product_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bought',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]

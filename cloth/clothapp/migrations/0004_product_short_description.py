# Generated by Django 5.1.1 on 2024-09-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothapp', '0003_product_is_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default=0),
        ),
    ]

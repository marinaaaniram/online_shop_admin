# Generated by Django 4.1.1 on 2022-09-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0003_rename_sum_order_order_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
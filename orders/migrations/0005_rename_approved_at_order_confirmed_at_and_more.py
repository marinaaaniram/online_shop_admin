# Generated by Django 4.1.1 on 2022-09-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='approved_at',
            new_name='confirmed_at',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('init', 'Init'), ('in_progress', 'In progress'), ('confirmed', 'Confirmed')], default='init', max_length=20),
        ),
    ]
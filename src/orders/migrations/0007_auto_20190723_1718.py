# Generated by Django 2.1.5 on 2019-07-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190422_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_address_final',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('shipped', 'Shipped')], default='created', max_length=120),
        ),
    ]
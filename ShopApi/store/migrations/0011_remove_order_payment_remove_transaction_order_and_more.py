# Generated by Django 4.1.7 on 2023-04-10 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_payment_balance'),
        ('store', '0010_remove_order_price_remove_order_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='store.transaction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='paymentMethod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.payment'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_payment_balance'),
        ('store', '0011_remove_order_payment_remove_transaction_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='paymentMethod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.payment'),
        ),
    ]

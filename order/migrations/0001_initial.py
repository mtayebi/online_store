# Generated by Django 4.0.2 on 2022-02-15 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0004_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('status', models.CharField(choices=[('Canceled', 'canceled'), ('Unpaid', 'unpaid'), ('Paid', 'paid')], default='Unpaid', max_length=8, verbose_name='basket_status')),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('code_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='code_title')),
                ('code_amount', models.PositiveIntegerField(verbose_name='code_amount')),
            ],
            options={
                'verbose_name': 'discount_code',
                'verbose_name_plural': 'discount_codes',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('number', models.PositiveIntegerField(verbose_name='order number')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.basket', verbose_name='order_basket')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='order_product')),
            ],
            options={
                'verbose_name': 'order_item',
                'verbose_name_plural': 'order_items',
            },
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_code',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.discountcode', verbose_name='basket_code'),
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='order_customer'),
        ),
    ]
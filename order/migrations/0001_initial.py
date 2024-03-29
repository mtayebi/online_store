<<<<<<< HEAD
# Generated by Django 4.0.2 on 2022-02-15 16:46
=======
# Generated by Django 4.0.2 on 2022-04-10 06:07
>>>>>>> frontend

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
<<<<<<< HEAD
        ('product', '0004_alter_product_discount'),
=======
        ('product', '0001_initial'),
>>>>>>> frontend
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('status', models.CharField(choices=[('Canceled', 'canceled'), ('Unpaid', 'unpaid'), ('Paid', 'paid')], default='Unpaid', max_length=8, verbose_name='basket_status')),
=======
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پاک شدن')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='پاک شده')),
                ('status', models.CharField(choices=[('Canceled', 'لغو شده'), ('Unpaid', 'پرداخت نشده'), ('Paid', 'پرداخت شده')], default='Unpaid', max_length=8, verbose_name='وضعیت سبد')),
>>>>>>> frontend
            ],
            options={
                'verbose_name': 'سبد',
                'verbose_name_plural': 'سبدها',
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پاک شدن')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='پاک شده')),
                ('code_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='عنوان کد')),
                ('code_amount', models.PositiveIntegerField(verbose_name='میزان تخفیف کد')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کدهای تخفیف',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پاک شدن')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='پاک شده')),
                ('number', models.PositiveIntegerField(verbose_name='تعداد سفارش')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.basket', verbose_name='سبد سفارش')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول سفارش')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_code',
<<<<<<< HEAD
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.discountcode', verbose_name='basket_code'),
=======
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.discountcode', verbose_name='کد تخفیف سبد'),
>>>>>>> frontend
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='مشتری این سفارش'),
        ),
    ]

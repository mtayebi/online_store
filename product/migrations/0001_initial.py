# Generated by Django 4.0.2 on 2022-02-14 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('cat_title', models.CharField(max_length=30, verbose_name='category_title')),
                ('about', models.TextField(max_length=500, verbose_name='about_category')),
                ('parent_cat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='parent_category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('discount_title', models.CharField(max_length=10, verbose_name='discount_title')),
                ('discount_amount', models.PositiveIntegerField(verbose_name='discount_amount')),
                ('type', models.CharField(choices=[('price', 'Price'), ('percent', 'Percent')], max_length=10, verbose_name='discount_type')),
                ('max_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='max_discount_value')),
            ],
            options={
                'verbose_name': 'discount',
                'verbose_name_plural': 'discounts',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('pro_name', models.CharField(max_length=40, verbose_name='product_name')),
                ('brand', models.CharField(max_length=30, verbose_name='brand')),
                ('image', models.ImageField(upload_to='', verbose_name='product_image')),
                ('properties', models.TextField(max_length=1000, verbose_name='properties')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='category')),
                ('discount', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.discount', verbose_name='discount')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['create_time'],
            },
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_discount_discount_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='price'),
            preserve_default=False,
        ),
    ]

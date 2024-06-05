# Generated by Django 5.0.6 on 2024-06-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                blank=True,
                help_text="Введите дату создания продукта (записи в БД)",
                null=True,
                verbose_name="Дата создания продукта (записи в БД)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price_per_purchase",
            field=models.PositiveIntegerField(
                help_text="Введите цену", verbose_name="Цена за покупку"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                blank=True,
                help_text="Введите дату последнего изменения продукта (записи в БД)",
                null=True,
                verbose_name="Дата последнего изменения продукта (записи в БД)",
            ),
        ),
    ]

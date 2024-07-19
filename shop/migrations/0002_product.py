# Generated by Django 5.0.6 on 2024-07-16 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Название")),
                ("brand", models.CharField(max_length=250, verbose_name="Бренд")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("slug", models.SlugField(max_length=250, verbose_name="URL")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=100, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="products/default.jpg",
                        upload_to="images/products/%Y/%m/%d",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Наличие"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["-created_at"],
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_image'),
        ('noon', '0002_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category'),
        ),
    ]

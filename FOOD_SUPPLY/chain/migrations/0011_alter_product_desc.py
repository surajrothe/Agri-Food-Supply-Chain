# Generated by Django 4.1.3 on 2022-12-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0010_rename_pub_date_product_manu_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]

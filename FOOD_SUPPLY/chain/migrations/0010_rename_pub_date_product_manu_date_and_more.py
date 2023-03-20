# Generated by Django 4.1.3 on 2022-12-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0009_auto_20221113_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pub_date',
            new_name='manu_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='product_price',
        ),
        migrations.AddField(
            model_name='product',
            name='cropused',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='farmer_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='farmer_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='process_used',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='product_qt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
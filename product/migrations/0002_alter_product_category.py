# Generated by Django 3.2 on 2021-05-07 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-09 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_photo_url', models.CharField(max_length=200)),
                ('product_price', models.PositiveIntegerField()),
                ('product_buy', models.BooleanField()),
            ],
        ),
    ]

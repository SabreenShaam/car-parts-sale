# Generated by Django 4.0.3 on 2022-07-07 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=180)),
                ('product_name', models.CharField(max_length=180)),
                ('unit_price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=180)),
                ('company', models.CharField(max_length=180)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=150)),
                ('total_payment', models.IntegerField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('delivery_time', models.TimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=180)),
                ('unit_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total_cost', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
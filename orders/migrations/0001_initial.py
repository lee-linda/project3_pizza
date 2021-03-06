# Generated by Django 2.0.3 on 2019-11-26 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('num_toppings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Regpizza', to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sicipizza', to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Additions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addition', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('small', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('category', models.CharField(max_length=64)),
                ('item', models.CharField(max_length=100)),
                ('additions', models.CharField(blank=True, max_length=500, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('quantity', models.IntegerField()),
                ('priceEach', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=64)),
                ('item', models.CharField(max_length=100)),
                ('additions', models.CharField(blank=True, max_length=500, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('quantity', models.IntegerField()),
                ('priceEach', models.DecimalField(decimal_places=2, max_digits=5)),
                ('orderStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderStatus', to='orders.OrderStatus')),
            ],
        ),
    ]

# Generated by Django 2.1.5 on 2020-06-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200607_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppings',
            name='order',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Order'),
        ),
    ]
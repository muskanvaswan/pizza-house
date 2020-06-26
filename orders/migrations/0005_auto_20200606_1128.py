# Generated by Django 2.1.5 on 2020-06-06 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_auto_20200606_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Food')),
                ('user', models.ManyToManyField(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='User',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='item',
        ),
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Order'),
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
# Generated by Django 4.1.5 on 2023-02-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.PositiveIntegerField(default=28201729, primary_key=True, serialize=False),
        ),
    ]

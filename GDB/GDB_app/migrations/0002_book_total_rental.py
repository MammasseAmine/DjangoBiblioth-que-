# Generated by Django 3.2 on 2021-07-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDB_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]

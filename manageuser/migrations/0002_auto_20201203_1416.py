# Generated by Django 3.1.3 on 2020-12-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
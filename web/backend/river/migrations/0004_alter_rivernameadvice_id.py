# Generated by Django 4.0 on 2022-01-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0003_rivernameadvice_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rivernameadvice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
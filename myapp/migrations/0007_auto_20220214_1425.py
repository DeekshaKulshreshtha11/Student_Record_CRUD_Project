# Generated by Django 3.1.14 on 2022-02-14 08:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220213_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='middle_name',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]

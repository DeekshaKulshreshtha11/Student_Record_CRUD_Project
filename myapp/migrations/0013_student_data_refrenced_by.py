# Generated by Django 3.1.14 on 2022-02-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20220214_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='refrenced_by',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 3.1.14 on 2022-02-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20220215_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='number_of_installment',
            field=models.PositiveIntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]

# Generated by Django 3.1.14 on 2022-02-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20220214_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='lateral',
            field=models.CharField(choices=[('REGULAR', 'REGUALR'), ('LATERAL ENTRY', 'LATERAL ENTRY')], max_length=50),
        ),
    ]

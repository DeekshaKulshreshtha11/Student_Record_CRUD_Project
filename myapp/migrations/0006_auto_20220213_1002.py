# Generated by Django 3.1.14 on 2022-02-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220210_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='domicile',
            field=models.FileField(blank=True, null=True, upload_to='d/9'),
        ),
        migrations.AddField(
            model_name='student_data',
            name='total_income',
            field=models.CharField(blank=True, choices=[('Income1', 'Income1'), ('Income2', 'Income3'), ('Income3', 'Income3'), ('Income4', 'Income4')], max_length=100, null=True),
        ),
    ]

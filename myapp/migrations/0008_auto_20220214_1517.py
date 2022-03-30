# Generated by Django 3.1.14 on 2022-02-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220214_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='category',
            field=models.CharField(choices=[('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('GENERAL', 'GENERAL'), ('MINORITY', 'MINORITY'), ('OHTER', 'OTHER')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='course',
            field=models.CharField(choices=[('B.tech', 'B.tech'), ('M.tech', 'M.tech'), ('BCA', 'BCA'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('Diploma', 'Diploma')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='total_income',
            field=models.CharField(blank=True, choices=[('Below 1 lac ', 'Below 1 lac'), ('1 lac - 2 lac', '1 lac - 2 lac'), ('2 lac - 4 lac', '2 lac - 4 lac'), ('Above 4 lac', 'Above 4 lac')], max_length=100, null=True),
        ),
    ]

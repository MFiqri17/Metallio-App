# Generated by Django 4.0.1 on 2022-01-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metallioApp', '0003_remove_profile_fname_remove_profile_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fullName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='universitas',
            name='kota',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='universitas',
            name='nama_univ',
            field=models.CharField(max_length=100),
        ),
    ]

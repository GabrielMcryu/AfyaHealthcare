# Generated by Django 4.1.3 on 2022-11-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0011_alter_region_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='county',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa')], max_length=255, null=True),
        ),
    ]

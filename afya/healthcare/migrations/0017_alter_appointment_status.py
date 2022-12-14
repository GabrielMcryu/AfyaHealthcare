# Generated by Django 4.1.3 on 2022-11-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0016_alter_appointment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Completed', 'Completed')], default='Pending', max_length=255),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-15 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0018_alter_appointment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appontment_date',
            new_name='appointment_date',
        ),
    ]
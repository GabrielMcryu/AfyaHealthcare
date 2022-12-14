# Generated by Django 4.1.3 on 2022-11-16 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0019_rename_appontment_date_appointment_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('tuesday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('wednesday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('thursday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('friday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('saturday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('sunday', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctorprofile')),
            ],
        ),
    ]

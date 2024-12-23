# Generated by Django 5.0.7 on 2024-07-19 11:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_chaivariety_delete_chaivarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aqi_variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('G', 'GOOD'), ('S', 'SATISFACTORY'), ('MO', 'MODERATE'), ('P', 'POOR'), ('VP', 'VERYPOOR'), ('SE', 'SEVERE')], default='ML', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='ChaiVariety',
        ),
    ]

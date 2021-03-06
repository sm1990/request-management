# Generated by Django 2.2.6 on 2020-04-15 09:34

from django.db import migrations, models
import src.incidents.models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0041_incident_current_decision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='current_severity',
            field=models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default=src.incidents.models.SeverityType('Low'), max_length=50),
        ),
    ]

# Generated by Django 2.2.6 on 2020-02-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0039_auto_20200229_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='refId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

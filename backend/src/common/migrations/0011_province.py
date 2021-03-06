# Generated by Django 2.2.1 on 2019-10-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_politicalparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sn_name', models.CharField(max_length=100)),
                ('tm_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]

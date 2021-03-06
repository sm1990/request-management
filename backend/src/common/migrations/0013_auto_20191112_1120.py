# Generated by Django 2.2.6 on 2019-11-12 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_category_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policestation',
            name='sn_division',
        ),
        migrations.RemoveField(
            model_name='policestation',
            name='tm_division',
        ),
        migrations.AlterField(
            model_name='policestation',
            name='district',
            field=models.ForeignKey(blank=True, db_column='district_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.District', to_field='code'),
        ),
        migrations.AlterField(
            model_name='policestation',
            name='division',
            field=models.ForeignKey(blank=True, db_column='division_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.PoliceDivision', to_field='code'),
        ),
    ]

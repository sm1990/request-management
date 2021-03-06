# Generated by Django 2.2.12 on 2020-04-28 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidents', '0046_auto_20200426_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='CannedResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SendCannedResponseWorkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('actioned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_sendcannedresponseworkflow_related', related_query_name='incidents_sendcannedresponseworkflows', to=settings.AUTH_USER_MODEL)),
                ('canned_response', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.CannedResponse')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_sendcannedresponseworkflow_related', related_query_name='incidents_sendcannedresponseworkflows', to='incidents.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

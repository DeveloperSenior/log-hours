# Generated by Django 4.0.4 on 2022-05-20 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogHoursApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogHoursApp.statuses', verbose_name='Estado'),
        ),
    ]

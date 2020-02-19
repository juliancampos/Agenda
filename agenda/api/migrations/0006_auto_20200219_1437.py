# Generated by Django 2.2.5 on 2020-02-19 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200219_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AlterField(
            model_name='period',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
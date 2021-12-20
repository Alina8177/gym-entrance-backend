# Generated by Django 4.0 on 2021-12-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='status',
            field=models.CharField(choices=[('success', 'Success'), ('canceled', 'Canceled')], default='success', max_length=10),
        ),
    ]

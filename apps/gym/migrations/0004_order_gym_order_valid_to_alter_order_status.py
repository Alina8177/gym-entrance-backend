# Generated by Django 4.0 on 2021-12-20 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='gym',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='gym.gym'),
        ),
        migrations.AddField(
            model_name='order',
            name='valid_to',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('paid', 'Paid')], default='open', max_length=10),
        ),
    ]

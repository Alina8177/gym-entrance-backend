# Generated by Django 4.0 on 2021-12-19 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('is_archive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gym', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='gym.gym')),
            ],
        ),
    ]

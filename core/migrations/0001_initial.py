# Generated by Django 4.2.10 on 2024-02-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Data de expiração')),
            ],
            options={
                'verbose_name': 'Alvo',
                'verbose_name_plural': 'Alvos',
            },
        ),
    ]

# Generated by Django 4.1 on 2022-08-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.SlugField(unique=True)),
                ('ExchangePrice', models.FloatField()),
                ('MinRecive', models.FloatField(null=True)),
                ('From', models.CharField(max_length=40)),
                ('To', models.CharField(max_length=40, null=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]

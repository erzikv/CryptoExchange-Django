# Generated by Django 4.1 on 2022-08-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.SlugField(unique=True)),
                ('Amount', models.FloatField()),
                ('AmountBack', models.FloatField()),
                ('TokenSend', models.CharField(max_length=40)),
                ('TokenWant', models.CharField(max_length=40)),
                ('PaymentStat', models.CharField(max_length=40, null=True)),
                ('SendSystemStat', models.CharField(max_length=40, null=True)),
                ('date_added_pay', models.DateTimeField()),
                ('TxnAddres', models.CharField(max_length=70, null=True)),
                ('CompString', models.CharField(max_length=40, null=True)),
                ('CancelString', models.CharField(max_length=40, null=True)),
                ('userIp', models.CharField(max_length=40)),
                ('is_limit', models.BooleanField(null=True)),
                ('meta_pay', models.BooleanField()),
                ('payeer_pay', models.BooleanField()),
            ],
        ),
    ]

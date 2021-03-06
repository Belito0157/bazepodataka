# Generated by Django 3.1.5 on 2021-01-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baze', '0011_artikal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otpremnica',
            fields=[
                ('brojotpremnice', models.IntegerField(primary_key=True, serialize=False)),
                ('napomena', models.CharField(max_length=25)),
                ('ukupno', models.IntegerField()),
                ('pib', models.IntegerField()),
                ('sifrazaposlenog', models.IntegerField()),
                ('brojnarudzbenice', models.IntegerField()),
                ('date', models.DateField()),
                ('brojracuna', models.IntegerField()),
            ],
        ),
    ]

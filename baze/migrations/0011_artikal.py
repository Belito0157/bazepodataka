# Generated by Django 3.1.5 on 2021-01-22 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baze', '0010_auto_20210122_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikal',
            fields=[
                ('sifraartikla', models.IntegerField(primary_key=True, serialize=False)),
                ('nazivartikla', models.CharField(max_length=25)),
                ('aktuelnacena', models.IntegerField()),
            ],
        ),
    ]

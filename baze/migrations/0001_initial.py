# Generated by Django 3.1.5 on 2021-01-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faktura',
            fields=[
                ('rednibroj', models.IntegerField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]

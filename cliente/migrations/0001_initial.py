# Generated by Django 5.0.6 on 2024-06-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('endereco', models.TextField()),
                ('data_nasc', models.DateField()),
            ],
        ),
    ]

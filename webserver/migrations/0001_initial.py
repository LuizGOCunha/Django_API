# Generated by Django 4.0 on 2021-12-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField(blank=True, null=True)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('bool', models.BooleanField(blank=True, null=True)),
                ('binary', models.BinaryField(blank=True, null=True)),
                ('observation', models.TextField(max_length=500)),
            ],
        ),
    ]

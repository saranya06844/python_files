# Generated by Django 4.1.4 on 2022-12-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_name', models.CharField(max_length=30)),
                ('Teacher_salary', models.FloatField()),
                ('Teacher_Address', models.CharField(max_length=100)),
            ],
        ),
    ]

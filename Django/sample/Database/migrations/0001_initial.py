# Generated by Django 4.1.4 on 2022-12-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_no', models.IntegerField()),
                ('Employee_name', models.CharField(max_length=30)),
                ('Employee_Salary', models.IntegerField()),
                ('Employee_Address', models.CharField(max_length=100)),
            ],
        ),
    ]

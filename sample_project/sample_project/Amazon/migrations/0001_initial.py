# Generated by Django 4.1.4 on 2022-12-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_RollNo', models.IntegerField()),
                ('Student_Name', models.CharField(max_length=30)),
                ('Student_Mark', models.FloatField()),
            ],
        ),
    ]

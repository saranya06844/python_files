# Generated by Django 4.1 on 2022-08-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Class', models.CharField(choices=[('sslc', 'SSLC'), ('plusone', 'PlusOne'), ('plustwo', 'PlusTwo')], default='SSLC', max_length=100)),
                ('Stu_Address', models.TextField(max_length=100)),
                ('Email_id', models.EmailField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=150, verbose_name='نام محموعه')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('Phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]

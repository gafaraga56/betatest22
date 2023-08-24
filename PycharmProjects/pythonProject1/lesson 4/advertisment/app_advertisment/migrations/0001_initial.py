# Generated by Django 4.2.4 on 2023-08-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Заговолок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('authors', models.CharField(max_length=64, verbose_name='автор')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата')),
            ],
        ),
    ]

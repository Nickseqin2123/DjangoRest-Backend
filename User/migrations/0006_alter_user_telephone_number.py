# Generated by Django 4.2.13 on 2024-06-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_user_birthday_alter_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=18, verbose_name='Номер телефона'),
        ),
    ]

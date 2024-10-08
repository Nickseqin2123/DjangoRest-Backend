# Generated by Django 4.2.13 on 2024-06-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_tag_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, error_messages={'max_length': 'Слишком длинный текст'}, max_length=85, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, error_messages={'max_length': 'Слишком длинный текст'}, max_length=60, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tag_user',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким тегом уже существует'}, max_length=20, unique=True, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.TextField(blank=True, error_messages={'max_length': 'Слишком длинный текст'}, max_length=50, verbose_name='О пользователе'),
        ),
    ]

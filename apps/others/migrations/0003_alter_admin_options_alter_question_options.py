# Generated by Django 4.2 on 2023-08-18 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'Админ', 'verbose_name_plural': 'Админы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]

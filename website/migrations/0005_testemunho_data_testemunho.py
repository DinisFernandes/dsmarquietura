# Generated by Django 3.2.7 on 2021-10-03 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20211003_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='testemunho',
            name='data_testemunho',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210915_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='referencia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem_post',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem De Perfil'),
        ),
    ]

from django.db import models
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

# Create your models here.

class Projeto(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    referencia = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    city =  models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    parish = models.CharField(max_length=100, blank=True, null=True, verbose_name='Freguesia')
    bathroom = models.IntegerField(default=0, blank=True, null=True, verbose_name='nº wc')
    bed = models.IntegerField(default=0, blank=True, null=True, verbose_name='nº quartos')
    garage = models.IntegerField(default=0, blank=True, null=True, verbose_name='nº garagem')
    construction = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Área de Construção')
    implantation = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,verbose_name='Área de Implantação')
    lote = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Área de Lote')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', verbose_name='Imagem De Perfil')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try :
            self.resize_image(self.imagem_post.name, 600)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        # if width <= new_width:
        #     img.close()
        #     return

        new_height = round(new_width * height / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)
        new_image.close()


class GaleriaPhotos(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    description = models.TextField(verbose_name='Descrição')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.resize_image(self.img.name, 600)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        # if width <= new_width:
        #     img.close()
        #     return

        new_height = round(new_width * height / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)
        new_image.close()


class Contact(models.Model):
    name = models.CharField(max_length=150)
    telefone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(default='mensagem')
    tratado = models.BooleanField(default=False)
    data_contact = models.DateTimeField(default=timezone.now, verbose_name='Data')

    def __str__(self):
        return self.name


class Testemunho(models.Model):
    name = models.CharField(max_length=150, verbose_name='nome')
    photo= models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True,
                                    verbose_name='Foto')
    job = models.CharField(max_length=150, blank=True, null=True, verbose_name='Profissão')
    testimony = models.TextField(verbose_name='testemunho')
    data_testemunho = models.DateTimeField(default=timezone.now, verbose_name='Data')

    def __str__(self):
        return self.name
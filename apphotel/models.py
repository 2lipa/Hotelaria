from django.core.validators import MinValueValidator
from django.db import models


class Locador(models.Model):
    nome = models.CharField(max_length=250, null=False, blank=False)
    pais = models.CharField(max_length=250, null=False, blank=False)
    cidade = models.CharField(max_length=250, null=False, blank=False)
    bairro = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.nome

class Local(models.Model):
    locador = models.ForeignKey('Locador', on_delete=models.CASCADE, related_name='locador')
    nome_local = models.CharField(max_length=50, null=True, blank=False)
    PROPRIEDADE_CHOICES = [
        ('Hotel', 'Hotel'),
        ('Pousada', 'Pousada'),
        ('Resort', 'Resort'),
        ('Fazenda', 'Fazenda'),
    ]
    propriedade = models.CharField(max_length=7, choices=PROPRIEDADE_CHOICES, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    NOTA_CHOICES = [
        ('Bom', 'Bom'),
        ('Médio', 'Médio'),
        ('Ruim', 'Ruim'),
    ]
    nota_avaliacao = models.CharField(max_length=6, choices=NOTA_CHOICES, null=False, blank=False)
    WIFI_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]
    wifi = models.CharField(max_length=3, choices=WIFI_CHOICES, null=False, blank=False)
    TV_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]
    tv = models.CharField(max_length=3, choices=TV_CHOICES, null=False, blank=False)
    CAMAS_CHOICE = [
        ('1 Cama de Solteiro', '1 Cama de Solteiro'),
        ('2 Camas de Solteiro', '2 Camas de Solteiro'),
        ('1 Cama de Casal', '1 Cama de Casal'),
        ('2 Camas de Casal', '2 Camas de Casal'),
        ('3 Camas de Solteiro', '3 Camas de Solteiro'),
    ]
    camas = models.CharField(max_length=50, choices=CAMAS_CHOICE, null=False, blank=False)
    descricao = models.CharField(max_length=400, null=True, blank=True)

class Reserva(models.Model):
    quarto = models.ManyToManyField('Local')
    data_entrada = models.DateField(null=False, blank=False)
    data_saida = models.DateField(null=False, blank=False)
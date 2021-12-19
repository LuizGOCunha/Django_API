from django.db import models

# Create your models here.


class Dados(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(blank=True, null=True)
    integer = models.IntegerField(blank=True,null=True)
    bool = models.BooleanField(blank=True,null=True)
    binary = models.BinaryField(blank=True, null=True)
    observation = models.TextField(max_length=500)

    def __str__(self):
        return f'id:{self.id}, nome:{self.nome}'


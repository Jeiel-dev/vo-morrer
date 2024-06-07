from django.db import models

class Produto(models.Model):
  cod_barra = models.CharField(max_length=20, unique=True ,blank=False)
  nome = models.CharField(max_length=100, blank=False)
  descricao = models.TextField(null=True,blank=True)
  valor = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.nome
  
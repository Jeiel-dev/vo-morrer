from django.db import models

class Cliente(models.Model):
  cpf = models.CharField(max_length=11, primary_key=True)
  nome = models.CharField(max_length=100, blank=False)
  cep = models.CharField(max_length=9, blank=False)
  endereco = models.TextField(blank=False)
  data_nasc = models.DateField(blank=False)
  
  def __str__(self):
      return self.nome
  
   
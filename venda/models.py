from django.db import models
from produto.models import Produto

class Item(models.Model):
  id = models.AutoField(primary_key=True)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.PositiveIntegerField(default=1)
  valor_total = models.DecimalField(max_digits=10, decimal_places=2)
  
  def calcular_valor_total(self):
        return self.produto.valor * self.quantidade

  def save(self, *args, **kwargs):
      self.valor_total = self.calcular_valor_total()
      super().save(*args, **kwargs)

  def __str__(self):
       return f"Item {self.id} - {self.produto.nome}"
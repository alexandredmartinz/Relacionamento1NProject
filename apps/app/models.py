from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50, null=False)
    

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome =models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length=50, null=False)
    preco = models.FloatField(null=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.descricao
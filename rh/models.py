from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Nota_Fiscal(models.Model):
    Data = models.DateField()
    Num_NF = models.IntegerField()
    Valor = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.Data} / ({self.Num_NF} - {self.Valor})'

class Cargo(models.Model):
    Cargo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.Cargo}'

class Folha_Pag(models.Model):
    Data = models.DateField()
    Hora_Extra = models.DecimalField(decimal_places=2, max_digits=10)
    Pagamento = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.Data} / ({self.Hora_Extra} - {self.Pagamento})'

class Colaborador(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
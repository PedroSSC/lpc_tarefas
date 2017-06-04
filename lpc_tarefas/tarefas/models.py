from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField('nome',max_length=200)
    email = models.CharField('nome',max_length=50)
    senha = models.CharField('nome',max_length=20)

    def __str__(self):
        return '{}'.format(self.nome)


class Projeto(models.Model):
    nome = models.CharField('nome',max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)

class ProjetoUsuario(models.Model):
    projeto = models.ForeignKey('Projeto')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.projeto)


class Tarefa(models.Model):
    nome = models.CharField('nome',max_length=200)
    dataEHoraDeInicio = models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    projeto = models.ForeignKey('Projeto', null = True)
    #usuario = models.ForeignKey('Usuario', null = True)

    def __str__(self):
        return '{}'.format(self.nome)

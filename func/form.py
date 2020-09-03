from django.forms import ModelForm
from .models import Transacao
from django import forms


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['email', 'nome', 'sobrenome', 'investimentos', 'imagem']

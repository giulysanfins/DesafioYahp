from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm

# Create your views here.
def paginaInicial(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']
    return render(request, "sites/index.html",data)


def visualizar(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, "sites/visualizar.html",data)

def cadastrar(request): #cadastrar
    data ={}
 #   form = TransacaoForm(request.POST or None) # se tiver algum form e errado ele volta, senao ele salva

  #  if form.is_valid():
   #     form.save()
    #    return cadastrar(request)
    #data['form'] =form
    return render(request,"sites/cadastrar.html")

def alterar(request):
    return render(request,"sites/alterar.html")

def linkar(request):
    return render(request,"sites/linkar.html")



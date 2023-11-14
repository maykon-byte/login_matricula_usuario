from django.shortcuts import render
from django.http import HttpResponse
from. models import Pessoa
from django.shortcuts import redirect
from django.contrib import messages

def matricula(request):
    if request.session.get('logado'):
        return render (request,'matricula.html')
    else:
        messages.add_message(request, messages.INFO, 'Faça Login Para Acessar o Sistema!' )
        return redirect('/usuario/login/')
    
def valida_matricula(request):
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        pessoa = Pessoa(nome=nome,
                        sobrenome=sobrenome,
                        email=email)   
        pessoa.save()
        messages.add_message(request, messages.constants.SUCCESS, 'Matrícula Realizada com Sucesso!' )
        return redirect('/usuario/matricula/')
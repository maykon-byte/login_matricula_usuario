from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages

def cadastro(request):
    return render (request,'cadastro.html')


def login(request):
    return render (request,'login.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, messages.constants.ERROR, 'Email ou Senha Inválido!' )
        return redirect('/usuario/cadastro/')
    
    if len(senha) < 8:
        messages.add_message(request, messages.constants.WARNING, 'Senha Deve Ter no Mínimo 8 Caracteres!' )
        return redirect('/usuario/cadastro/')
    
    usuario= Usuario.objects.filter(email = email)

    if len(usuario) >0:
        messages.add_message(request, messages.constants.WARNING, 'Email ja Cadastrado!' )
        return redirect('/usuario/cadastro/')
    try:
        senha = sha256(senha.encode()).hexdigest()

        usuario = Usuario(nome= nome,
                        email=email,
                        senha=senha)
        usuario.save()
        messages.add_message(request, messages.constants.SUCCESS, 'Cadastro Realizado com Sucesso!' )
        return redirect('/usuario/cadastro/')
    except:
        messages.add_message(request, messages.constants.ERROR, 'Erro Interno do Sistema!' )
        return redirect('/usuario/cadastro/')
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    senha = sha256(senha.encode()).hexdigest()

    usuario= Usuario.objects.filter(email = email).filter(senha=senha)

    if len(usuario) == 0:
        messages.add_message(request, messages.constants.WARNING, 'Email ou Senha Inválido!' )
        return redirect('/usuario/login/')
    elif len(usuario) > 0:
        request.session['logado']=True
        request.session['usuario_id']=usuario[0].id
        return redirect('/usuario/matricula')

def sair(request):
    request.session.flush()
    messages.add_message(request, messages.constants.WARNING, 'Você Precisa Estar Logado No Sistema!' )
    return redirect('/usuario/login/')
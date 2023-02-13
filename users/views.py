from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    #capturando URL
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})

def validate(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    registration = request.POST.get('registration')
    password = request.POST.get('password')

    #filtro necessário para verificação do e-mail já existente no banco.
    user = User.objects.filter(email = email)

    #verificando se o usuário digitou um nome e um e-mail.
    if len(name.strip()) == 0 or len(email.strip()) == 0: 
        return redirect('/usuario/cadastro/?status=1')

    if len(password) < 8:
        return redirect('/usuario/cadastro/?status=2')

    #verificando se o usuário digitou um e-mail que já está cadastrado.
    if len(user) > 0:
        return redirect('/usuario/cadastro/?status=3')

  
    try:
                    #binary                 #hexa64
        password = sha256(password.encode()).hexdigest()
        user = User(name = name, 
                email = email, 
                registration = registration,
                password = password )
        user.save()

        return redirect ('/usuario/login/')

    except:
        return redirect ('/usuario/cadastro/?status=4')


def validateLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    user = User.objects.filter(email = email).filter(password = password)

    if len(user) == 0:
        return redirect('/usuario/login/?status=1')
    
    elif len(user) > 0:
        #session, uma váriavel global do sistema
        #armazenando nela o ID do usuário
        request.session['user'] = user[0].id 
        return redirect('/eventos/home')

    return HttpResponse(f'{email} {password}')

def recover(request):
    status = request.GET.get('status')

    return render(request, 'recover.html', {'status': status})

def validateRecover(request):
    email = request.POST.get('email')

    user = User.objects.filter(email = email)
    
    if len(user) == 0:
        return redirect('/usuario/recover/?status=1')
    
    elif len(user) > 0:
        #session, uma váriavel global do sistema
        #armazenando nela o ID do usuário
        request.session['user'] = user[0].id 
        return redirect('/usuario/login/?status=3')

def leave(request):
    #usuário saiu do sistema, session é limpa
    #por completa
    request.session.flush()
    return redirect ('/usuario/login/')
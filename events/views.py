from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import User
from .models import Eventos
from datetime import date, datetime, timedelta
from .forms import AddEvent
from django.http import Http404
from django.core.paginator import Paginator


def home(request):
    #segurança, verificar se o usuário está logado.
    status = request.GET.get('status')
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        paginator = Paginator(events, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'home.html', {'Eventos': events, 'user': user, 'status': status, 'page': page, 'today': dateToday})
    else:
        return redirect('/usuario/login/?status=2')

def allEvents(request):
    #segurança, verificar se o usuário está logado.
    status = request.GET.get('status')
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        paginator = Paginator(events, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)

        return render(request, 'allEvents.html', {'page': page, 'user': user, 'status': status, 'today': dateToday})

    else:
        return redirect('/usuario/login/?status=2')

def addEvent(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        form = AddEvent()
        form.fields['user'].initial = request.session['user']
        form.fields['tipo'].initial = 'Evento'
        return render(request, 'addEvent.html', {'form': form, 'user': user})
    else:
        return redirect('/usuario/login/?status=2')

def addClassroom(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        form = AddEvent()
        form.fields['user'].initial = request.session['user']
        form.fields['tipo'].initial = 'Aula'
        return render(request, 'addClassroom.html', {'form': form, 'user': user})
    else:
        return redirect('/usuario/login/?status=2')


def today(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(registrationDate = dateToday)
        size = 0
        classroomsNum = 0
        eventsNum = 0

        for counter in events:
            size = size+counter.meals

        for counter in events:
            if counter.tipo == 'Aula':
                classroomsNum = classroomsNum + 1
        
        for counter in events:
            if counter.tipo == 'Evento':
                eventsNum = eventsNum + 1

        paginator = Paginator(events, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'today.html',
                             {'Eventos': events, 'today': dateToday, 'user': user, 'page': page, 'size': size, 'classrooms': classroomsNum, 'eventsNum': eventsNum}) 
    else:
        return redirect('/usuario/login/?status=2')



def about(request):
    
    return render (request, 'about.html')


def week(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter()
        eventsFilterMonth = set()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)


        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'week.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def month(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)

        #converter para lista, uma vez que não dá para sobrecarregar o set.
        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'month.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')
    

def year(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'year.html',
                             {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def weekUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilterMonth = set()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)


        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def monthUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)

        #converter para lista, uma vez que não dá para sobrecarregar o set.
        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')
    

def month(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)

        #converter para lista, uma vez que não dá para sobrecarregar o set.
        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'month.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')
    

def year(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'year.html',
                             {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def weekUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilterMonth = set()
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)


        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def monthUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)

        #converter para lista, uma vez que não dá para sobrecarregar o set.
        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def yearUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'yearUser.html',
                             {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def events(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(tipo = 'Evento')

        paginator = Paginator(events, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'allEventsEvents.html',
                                    {'Eventos': events, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def eventsToday(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(registrationDate = dateToday)
        eventsFilter = set()
        size = 0
        eventsNum = 0

        for filter in events:
            if filter.tipo == 'Evento':
                eventsFilter.add(filter)
                eventsNum = eventsNum+1
        

        for filter in eventsFilter:
            size = size+filter.meals
        
        

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'todayEvents.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page, 'size': size, 'eventsNum':eventsNum}) 
    else:
        return redirect('/usuario/login/?status=2')

def classroomsToday(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(registrationDate = dateToday)
        eventsFilter = set()
        size = 0
        classrooms = 0

        for filter in events:
            if filter.tipo == 'Aula':
                eventsFilter.add(filter)
                classrooms = classrooms+1
        

        for filter in eventsFilter:
            size = size+filter.meals
        
        

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'todayClassrooms.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page, 'size': size, 'classrooms':classrooms}) 
    else:
        return redirect('/usuario/login/?status=2')

def weekUserEvents(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilterMonth = set()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)
        
        for filter in events:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)
            

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)


        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekUserEvents.html',
                                    {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def monthUserEvents(request):
     #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthUserEvents.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def yearUserEvents(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'yearUserEvents.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')



def weekUserClassrooms(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilterMonth = set()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)
        

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)
        
        for filter in events:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)


        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekUserClassrooms.html',
                                    {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def monthUserClassrooms(request):
     #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthUserClassrooms.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def yearUserClassrooms(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'yearUserClassrooms.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def weekClassrooms(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilterMonth = set()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)

        
        for filter in eventsFilter:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)


        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekClassrooms.html',
                                    {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def weekEvents(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilterMonth = set()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilterMonth.add(filter)

        for filter in eventsFilterMonth:
            if filter.registrationDate.day == dateToday.day:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+1:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+2:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+3:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+4:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+5:
                eventsFilter.add(filter)
            if filter.registrationDate.day == dateToday.day+6:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)


        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'weekEvents.html',
                                    {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def monthClassrooms(request):
     #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthClassrooms.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def yearClassrooms(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Aula':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'yearClassrooms.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def monthEvents(request):
     #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.month == dateToday.month:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'monthEvents.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def yearEvents(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.all()
        eventsFilter = set()
        eventsFilterTwo = set()

        for filter in events:
            if filter.registrationDate.year == dateToday.year:
                eventsFilter.add(filter)
        
        for filter in eventsFilter:
            if filter.tipo == 'Evento':
                eventsFilterTwo.add(filter)

        eventsFilterTwo = list(eventsFilterTwo)
        paginator = Paginator(eventsFilterTwo, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'yearEvents.html',
                             {'Eventos': eventsFilterTwo, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')




def classrooms(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(tipo = 'Aula')

        paginator = Paginator(events, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'allEventsClassrooms.html',
                                    {'Eventos': events, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def eventsUser(request):
   #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()

        for filter in events:
            if filter.tipo == 'Evento':
                eventsFilter.add(filter)

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'allEventsEventsUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')

def classroomsUser(request):
    #segurança, verificar se o usuário está logado.
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        dateToday = date.today()
        events = Eventos.objects.filter(user = user)
        eventsFilter = set()

        for filter in events:
            if filter.tipo == 'Aula':
                eventsFilter.add(filter)

        eventsFilter = list(eventsFilter)
        paginator = Paginator(eventsFilter, 8)
        page_num =  request.GET.get('page')
        page = paginator.get_page(page_num)
        return render(request, 'allEventsClassroomsUser.html',
                                    {'Eventos': eventsFilter, 'today': dateToday, 'user': user, 'page': page}) 
    else:
        return redirect('/usuario/login/?status=2')


def registerEvent(request):
    #impedir usuário de acessar a URL sem usar o submit
    if request.method == 'POST':
        #coletando dados via post do formulário
        form = AddEvent(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/eventos/home/?status=2')
        else:
            return HttpResponse('error')


def update(request, id):
    #usar filter para obter objeto iteravel
    
    if request.method == 'GET':
            user = User.objects.get(id = request.session['user'])
            evento = Eventos.objects.filter(id = id)
            events = Eventos.objects.get(id = id)
            if user == events.user:
                form = AddEvent(instance = events)
                form.fields['user'].initial = request.session['user']
                form.fields['tipo'].initial = 'Aula'

                return render(request, 'editEvent.html', {'form': form, 'event': events, 'evento:': evento, 'user': user})
            
            elif user.tipo == "admin":
                form = AddEvent(instance = events)
                form.fields['user'].initial = request.session['user']
                form.fields['tipo'].initial = 'Aula'

                return render(request, 'editEvent.html', {'form': form, 'event': events, 'evento:': evento, 'user': user})
            
            else:
                return redirect('/eventos/all/?status=2')
        
    elif request.method == 'POST':
        events = Eventos.objects.get(id = id)
        form = AddEvent(request.POST, instance = events)

        if form.is_valid():
            form.save()
            return redirect('/eventos/home/?status=3')
        else:
            return HttpResponse('error')

    """ else:
        return redirect('/usuario/login/?status=2') """


def delete(request, id):
    if request.session.get('user'):
        user = User.objects.get(id = request.session['user'])
        events = Eventos.objects.get(id = id)
        if user == events.user:
            events = Eventos.objects.get(id = id).delete()
            
            return redirect('/eventos/home/?status=1')
        
        else:
            return redirect('/eventos/all/?status=1')
    else:
        return redirect('/usuario/login/?status=3')
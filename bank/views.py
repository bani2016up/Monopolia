from math import remainder
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import addForm


# Create your views here.
def home(request):
    item = Banck_account.objects.order_by('-balanc')
    
    data = {'item': item}
    return render(request, 'main.html', data)

def buy(request, id):
    account = get_object_or_404(Banck_account, id=id)
    if request.method == 'POST':
        form = addForm(request.POST) 
        summa = int(form.data['summa']) 
        formpin = int(form.data['pin'])
        pin = account.pin
        if form.is_valid() and pin == formpin:
            balanc = account.balanc
            balanc = balanc + summa
            account.balanc = balanc
            account.save()
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Вам не хватет денег или Ваш пин не верен.')
    else: 
        form = addForm()   
        balanc = get_object_or_404(Banck_account, id=id)
    data = {'form': form,
            }
    return render(request, 'sale.html', data)

def sale(request, id):
    account = get_object_or_404(Banck_account, id=id)
    if request.method == 'POST':
        form = addForm(request.POST) 
        summa = int(form.data['summa']) 
        formpin = int(form.data['pin'])
        pin = account.pin
        if form.is_valid() and account.balanc >= summa and pin == formpin:
            balanc = account.balanc
            balanc = balanc - summa
            account.balanc = balanc
            account.save()
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Вам не хватет денег или Ваш пин не верен.')
    else: 
        form = addForm()   
        balanc = get_object_or_404(Banck_account, id=id)
    data = {'form': form,
            }
    return render(request, 'sale.html', data)

def restart(reqest):
    item = Banck_account.objects.all()
    for i in item:
        i.balanc = 10000
        i.save()
    
    return redirect('/')

def makesure(request):
    return render(request, 'makesure.html')
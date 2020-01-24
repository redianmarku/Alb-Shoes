from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Produkt, ProdukteReja, Shporta, Profile
from django.db.models import Sum


def kryefaqja(request):
    produktet = Produkt.objects.all()
    new_produkt = ProdukteReja.objects.all()
    context = {
        'title':'Kryefaqja',
        'produktet': produktet,
        'new_produkt': new_produkt
    }
    return render(request, 'e_web/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('kreu:home')
        else:
            messages.error(request, f'Username ose Password nuk eshte i sakte!')
            return redirect('kreu:login')
    context = {
        'title':'Login'
    }
    return render(request, 'e_web/login.html', context)


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password1'])
            auth.login(request, user)
            return redirect('kreu:home')
        else:
            messages.error(request, f'Format e passwordit nuk jane te njejta ose emaili nuk eshte funksional!')
            return redirect('kreu:register')

    else:
        form = Register()
        

    context = {
        'title':'Regjistrohu',
        'form':form
    }
    return render(request, 'e_web/register.html', context)


@login_required(login_url='kreu:login')
def logout(request):
    auth.logout(request)
    return redirect('kreu:home')


def produkte(request):
    context = {
        'title':'Regjistrohu',
    }
    return render(request, 'e_web/product.html', context)


def kategorite(request):
    produktet = Produkt.objects.all()
    context = {
        'title':'Kategorite',
        'produktet': produktet
        }
    return render(request, 'e_web/category.html', context)


@login_required(login_url='kreu:login')
def shporta(request):
    current_user = request.user
    shporta = Profile.objects.filter(user=current_user)
    tot_num = shporta
    total = Sum(tot_num)
    new_produkt = ProdukteReja.objects.all()
    
    context = {
        'title':'Shporta', 
        'shporta': shporta, 
        'total': total ,
        'new_produkt': new_produkt
    }
    return render(request, 'e_web/cart.html', context)


def pagesa(request):
    context = {
        'title':'Pagesa', 
    }
    return render(request, 'e_web/checkout.html', context)


def kontakt(request):
    context = {
        'title':'Kontakt',
    }
    return render(request, 'e_web/contact.html', context)


@login_required(login_url='kreu:login')
def fshij(request, produkt_id):
    Profile.objects.filter(produkt_id=produkt_id).delete()
    return redirect('kreu:shporta')
    

@login_required(login_url='kreu:login')
def shto_shport(request, produkt_id):
    current_user = request.user
    produkt_model = Produkt.objects.get(id=produkt_id)
    Profile.objects.create(user=current_user, produkt=produkt_model)
    return redirect('kreu:shporta')

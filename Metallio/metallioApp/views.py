from asyncio.proactor_events import constants
from email.headerregistry import Group
from multiprocessing import context
from pickletools import read_uint1
from django.shortcuts import render, redirect
from .models import *
from .forms import RegisterForm, ProfileRegisterForm, MetallioRegisterForm, Pilihan1, Pilihan2
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unatuheticated_user, allowed_users, admin_only



# Create your views here.
@login_required(login_url='login')
@admin_only
def dashboard(request):
    peserta = Profile.objects.all()
    total_peserta = peserta.count()
    context = {'peserta': peserta, 'total_peserta': total_peserta}
    return render(request, 'metallioApp/dashboard.html', context)


def Register(request):
    user_form = RegisterForm()
    profile_form = ProfileRegisterForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit= False)
            
            
            # assign user to profile
            profile.user = user
            profile.email = user.email
            profile.save()
            group = Group.objects.get(name='Peserta')
            user.groups.add(group)            
            return redirect('login')
        
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
    
    context = {'user':user_form, 'profile':profile_form}
    return render(request, 'metallioApp/register.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        else:
            messages.info(request, 'Username OR Password incorrect')
    
    context  = {}
    return render(request, 'metallioApp/login.html', context)


def Events(request, pk):
    peserta = Profile.objects.get(id = pk)
    context = {'peserta':peserta}
    return render(request, 'metallioApp/eventList.html', context)


def Beranda(request, pk):
    peserta = Profile.objects.get(id = pk)
    context = {'peserta': peserta}
    return render(request, 'metallioApp/beranda.html', context)
        
        
def MetallioRegis(request, pk):
    peserta = Profile.objects.get(id = pk)
    # ptn = Universitas.objects.get(id = pk) 
    form = MetallioRegisterForm(instance=peserta)
    # form_pilihan = MetallioRegisterForm(instance=form_ptn)
    if request.method == "POST":
        form = MetallioRegisterForm(request.POST, instance=peserta)
        # form_pilihan = MetallioRegisterForm(request.POST, instance=form_ptn)
        if form.is_valid():
            form.save()
            return redirect('DaftarPilihan', pk = peserta.id) 
    context = {"form":form}   
    return render(request, 'metallioApp/daftarMetallio.html', context)


def MetallioPilihan(request, pk):
    peserta = Profile.objects.get(id = pk)
    form1 = Pilihan1(instance=peserta)
    form2 = Pilihan2(instance=peserta)
    
    if request.method == "POST":
        form1 = Pilihan1(request.POST, instance=peserta)
        form2 = Pilihan2(request.POST, instance=peserta)
        
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('beranda', pk = peserta.id)
    context = {"form1":form1, "form2":form2}   
    return render(request, 'metallioApp/daftarPilihan.html', context)      





    
                   
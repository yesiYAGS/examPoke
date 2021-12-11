from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
import bcrypt
from poke.models import *
from datetime import datetime, time, timezone
from time import gmtime, strftime


def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    
    if 'u_id' not in request.session:
        request.session['u_id'] = 0

    return render(request, 'index.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def reg_validate(request):
    if request.method == 'POST':
        errorescome= User.objects.Validaciones_login(request.POST)
        if errorescome :
            print(errorescome)
            for error_key, error_value in errorescome.items():
                messages.error(request, error_value, extra_tags= error_key) 
            return render(request, 'index.html')
        else:
            user= User.objects.filter(email=request.POST['email'])
            if user:
                print('email are ok')
                messages.error(request,'error de login')
                return render(request, 'index.html')
            else:

                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                new_user = User.objects.create(first_name = request.POST['first_name'], alias = request.POST['alias'], email = request.POST['email'], register_date = request.POST['register_date'], password = pw_hash)
                print(new_user)
                request.session['u_id'] = new_user.id
                #save User._id in session
                messages.success(request, 'You have registered succesfully. You may now login', extra_tags = 'registered')
                return redirect('/pokes')
        

    return redirect('/')

def login_validate(request):
        email = request.POST["email"]
        password = request.POST["password"]
        print(f"{email} {password}")
        echeck = User.objects.filter(email=email) 
        print (echeck)
        if echeck:
            print('existe')
            #if echeck[0].password == password:
            if bcrypt.checkpw(request.POST['password'].encode(), echeck[0].password.encode()):
                print(echeck[0].password)
                request.session['login'] = True
                request.session['u_id'] = echeck[0].id
                return redirect('/pokes')
            else:
                print('passwor bad')
                messages.error(request,'Password invalido', extra_tags = 'badpas')
                return redirect('/')

        else: 
            messages.error(request,'Email No registrado', extra_tags = 'malem')
            return redirect('/')
            

#*******************************************************************************

def pokes(request):
    user = User.objects.get(id=request.session['u_id'])
    usuario = User.objects.all()
    
    context = {
        'user': user,
        'usuario':usuario,
    }
    return render(request, 'pokes.html', context)

def allpokes(request):
    suma = request.POST["suma"]
    if suma == "sumas":
        request.session['u_id']= request.session['u_id']+ 1
        # request.session['u_id']= 0+ 1 solo suma una vez 

    # se logra sumar pero solo la cantidad de usuarios que hay :( 
    # ademas las veces que se oprime el boton le suma uno a todos y cambia el usuario que esta registrado 
    return redirect('/pokes')

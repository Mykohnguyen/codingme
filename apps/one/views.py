from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt
import random

from datetime import date
from pet_ninja import settings
import datetime
import stripe

from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request,'one/home.html')
def register(request):
    return render(request,'one/register.html')
def registering(request):
    if request.method=='POST':
        result = User.objects.validations(request.POST)
        if 'errors' in result:
            for key,value in result['errors'].items():
                messages.error(request,value)           
        else:
            messages.success(request,'You have successfully registered')
        return redirect('/register')
    return redirect('/')
def logging_in(request):
    if request.method=='POST':
        users_with_same_email = User.objects.filter(email=request.POST['email'])
        if len(users_with_same_email) > 0:
            user_1=users_with_same_email.first()
            if bcrypt.checkpw(request.POST['password'].encode(),user_1.password.encode()):
                request.session['id'] = user_1.id
                request.session['display_name'] = user_1.display_name
                return redirect('/user')
            else:
                messages.error(request,'Wrong password')
                return redirect('/invalid')
        else:
            messages.error(request,'Email does not exist')
            return redirect('/invalid')

def invalid(request):
    return render(request,'one/invalid.html')

def user_page(request):
    if "id" not in request.session:
        return redirect('/')
    user =  User.objects.get(id=request.session['id'])
    weapons_user_has = user.weapons.all()
    auras_user_has = user.auras.all()
    backgrounds_user_has = user.backgrounds.all()
    if user.favorite_weapon != "":
        favorite_weapon = Weapon.objects.get(name=user.favorite_weapon)
    else:
        favorite_weapon = "";
    if user.favorite_aura != "":
        favorite_aura = Aura.objects.get(name=user.favorite_aura)
    else:
        favorite_aura = "";
    if user.favorite_background != "":
        favorite_background = Background.objects.get(name=user.favorite_background)
    else:
        favorite_background = "";

    context = {
        'weapons_owned': weapons_user_has,
        'auras_owned':auras_user_has,
        'backgrounds_owned':backgrounds_user_has,
        'favorite_weapon': favorite_weapon,
        'favorite_aura': favorite_aura,
        'favorite_background':favorite_background
    }
    return render(request,'one/user.html',context)

def user_info(request):
    if "id" not in request.session:
        return redirect('/')
    user =User.objects.get(id=request.session['id'])
    today = date.today()
    age= today.year - user.dob.year - ((today.month,today.day) < (user.dob.month, user.dob.day))
    context = {
        'user':user,
        'age':age
    }
    return render(request,'one/user_info.html',context)
def view_user(request,userid):
    if "id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=userid)
    if user.favorite_weapon != "":
        favorite_weapon = Weapon.objects.get(name=user.favorite_weapon)
    else:
        favorite_weapon = "";
    if user.favorite_aura != "":
        favorite_aura = Aura.objects.get(name=user.favorite_aura)
    else:
        favorite_aura = "";
    if user.favorite_background != "":
        favorite_background = Background.objects.get(name=user.favorite_background)
    else:
        favorite_background = "";
    today = date.today()
    age= today.year - user.dob.year - ((today.month,today.day) < (user.dob.month, user.dob.day))
    context = {
        'user':user,
        'age':age,
        'favorite_background':favorite_background,
        'favorite_aura':favorite_aura,
        'favorite_weapon':favorite_weapon
    }
    return render(request,'one/view_user.html',context)
    
def user_info_edit(request):
    user= User.objects.get(id=request.session['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.display_name = request.POST['display_name']
    user.email = request.POST['email']
    user.programming_language= request.POST['programming_language']
    user.location = request.POST['location']
    user.save()
    return redirect('/user/info')
    
def user_edit(request):
    if "id" not in request.session:
        return redirect('/')
    user =User.objects.get(id=request.session['id'])
    context = {
        'user':user
    }   
    return render(request,'one/user_edit.html',context)

def ranking_page(request):
    if "id" not in request.session:
        return redirect('/')
    everyone = User.objects.order_by("-point")
    context = {
        'peoples': everyone
    }
    return render(request,'one/ranking.html',context)
def classroom(request):
    if "id" not in request.session:
        return redirect('/')
    return render(request,'one/classroom.html')
def mall(request):
    if "id" not in request.session:
        return redirect('/')
    golds = Gold.objects.all()
    context = {
        'stripe_key': settings,
        'golds': golds
    }
    return render(request,'one/mall.html',context)
def mall_weapon(request,category):
    if "id" not in request.session:
        return redirect('/')
    if(category == "weapon"):
        allItems = Weapon.objects.all();
    elif(category == "aura"):
        allItems = Aura.objects.all();
    elif(category == "background"):
        allItems = Background.objects.all();
    category = category
    context={
        'weapons': allItems,
        'category': category
    }
    print(context)
    return render(request,'one/mall_weapon.html',context)
      
def python_easy(request):
    if "id" not in request.session:
        return redirect('/')
    return render(request,'one/classroom_python_easy.html')
    
def language(request,language,difficulty,number):
    if "id" not in request.session:
        return redirect('/')
    q = Question.objects.filter(category=language,difficulty= difficulty)
    q = q.get(id=number)
    a = Answer.objects.filter(question=number)
    context = {
        'questions': q,
        'answers':a
    }
    return render(request,'one/classroom_python_easy.html',context)

def adding(request):

    return render(request,'one/adding.html')

def addinga(request):
    Answer.objects.create(
        content = request.POST['content'],
        correct= request.POST['correct'],
        question_id=request.POST['question_id']
    )
    return redirect('/adding')
def addingq(request):
    Question.objects.create(
        content=request.POST['content'],
        difficulty=request.POST['difficulty']
        )
    return redirect('/adding')
def check_answers(request):  
    if "count" not in request.session:
        request.session['count'] = 0;
    if request.POST['selected'] == 'True':
        request.session['count'] += 1
    if int(request.POST['number']) + 1 > 10:
        return redirect('/classroom/end_of_quiz')
    
    return redirect ('/classroom/{}/{}/{}'.format(request.POST['category'],request.POST['difficulty'],int(request.POST['number']) + 1))
def end_of_quiz(request):
    if "id" not in request.session:
        return redirect('/')
    u = User.objects.get(id=request.session['id'])
    u.point+=request.session['count']
    u.gold+= request.session['count']
    u.save()
    return render(request,'one/endofquiz.html')

def ending(request):
    request.session['count'] = 0

    return redirect('/user')

def buy_item(request,category,id):
    user = User.objects.get(id=request.session['id'])
    if(category == "weapon"):
        item_being_bought = Weapon.objects.get(id=id)
    elif(category == "aura"):
        item_being_bought = Aura.objects.get(id=id)
    elif(category == "background"):
        item_being_bought = Background.objects.get(id=id)

    if user.gold >= item_being_bought.price:
        item_being_bought.owner.add(request.session['id'])
        item_being_bought.save()
        user.gold -= item_being_bought.price
        user.save()
    else:
        alert('Not enough gold!')
    return redirect('/user')
def charge(request):
    if request.method == "POST":
        token    = request.POST.get("stripeToken")

    try:
        charge  = stripe.Charge.create(
            amount      = int(request.POST['price'],0),
            currency    = "usd",
            source      = token,
            description = "The product charged to the user"
        )
    except stripe.error.CardError as ce:
        return False, ce

    else:
        user = User.objects.get(id=request.session['id'])
        user.gold += int(request.POST['amount'])
        user.save()
        return redirect('/user')

def favorite_weapon(request,category):
    user = User.objects.get(id=request.session['id'])
    if(category == "weapon"):
        item = Weapon.objects.get(image=request.POST['name'])
        user.favorite_weapon = item.name
    elif(category == "aura"):
        item= Aura.objects.get(image=request.POST['name'])
        user.favorite_aura = item.name
    elif(category == "background"):
        item= Background.objects.get(image=request.POST['name'])
        user.favorite_background = item.name
    
    user.save()
    return redirect('/user')

def logout(request):

    request.session.clear();
    return redirect('/')



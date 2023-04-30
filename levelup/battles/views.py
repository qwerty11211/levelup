import openai,os,json
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import User, Battle,History, Checkin, Money

from django.utils import timezone
import random

def user_exist(credential):
    username = credential.cleaned_data.get("username")
    password = credential.cleaned_data.get("password")
    user = User.objects.filter(username=username, password=password)
    if user:
        return True
    else:
        return False


def valid_username(credential):
    username = credential.cleaned_data.get("username")
    user = User.objects.filter(username=username)
    if user:
        return False
    else:
        return True


def login_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if user_exist(form):
                messages.add_message(request, messages.INFO, 'Logged in!')
                return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def register_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and valid_username(form):
            form.save()
            return redirect('/user/login')
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def home(request):
    money = Money.objects.filter().order_by('-money')
    battles = Battle.objects.all().order_by('end_date')
    return render(request, 'home.html', {'battles': battles,'money':money})



def create_battle(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        end_date = request.POST['end_date']
    
        challenge_amount = request.POST['challenge_amount']
        created_by = 1
        
        Battle.objects.create(name=name, description=description, end_date=end_date,
                              challenge_amount=challenge_amount, created_by=created_by)

        return redirect( 'home')
    else:

        return render(request, 'create_battle.html')




def battle_details(request, id):
    battle = Battle.objects.get(id=id)
    history=History.objects.filter(battle_id=id)

    context = {
        'battle': battle,
        'history': history,
        'won':False
        
    }
    current_date = timezone.now().date()

    if current_date>=battle.end_date.date():
        if random.randint(1, 100)==Battle.created_by:
           context['won']=True
          


    return render(request, 'battle-details.html', context)

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        my_model = Checkin.objects.create(image=image)
 
        return redirect('success')
    return render(request, 'upload_image.html')

def minted_nft(request):
  
    nft_details=json.loads(minted_nft)["nfts_minted"]["NFT details"]
    return render(request, 'view_minted_nft.html', {'nft_details': nft_details})
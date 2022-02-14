from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from news_app.models import News
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    news=News.objects.all()
    return render(request, 'news/home.html' , context={'news':news})


@login_required()
def add(request):
    if request.method == 'GET':

        return render(request, 'news/add.html')
    else:
        title = request.POST['title']
        description= request.POST['description']
        News.objects.create(title=title, description=description, user_id=request.user.id)
        
        return redirect('home')


def edit(request, id):
    news=News.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'news/edit.html', context={'news':news})
    else:
        title=request.POST['title']
        description=request.POST['description']
        news.title=title
        news.description=description
        news.save()
        
        return redirect('home')


def delete(request, id):
    news=News.objects.get(id=id)
    news.delete()
    return redirect ('home')

def register(request):
    if request.method == 'GET':
        return render(request, 'login/register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        
        
        send_mail('Account Created',
        f'Your account has been created with username {username} ',
        settings.EMAIL_HOST_USER,
        ['manjil.gautam180@gmail.com', email],
        fail_silently=False,
        )

        return redirect('login')






def signin(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')

            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)
        else:
            return redirect('login')
@login_required
def profile(request):
    user= User.objects.get(id=request.user.id)
    return render(request, 'login/profile.html', context={'user':user})

@login_required
def reset(request):
    if request.method == 'GET':
        return render(request, 'login/reset.html')
    else:
        new_password= request.POST['password']
        user= User.objects.get(id=request.user.id)
        user.set_password(new_password)
        user.save()
        return redirect('home')



def signout(request):
    logout(request)
    return redirect('login')


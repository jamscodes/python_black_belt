from django.shortcuts import render, redirect
from .models import Wish, Like
from login_app.models import User

# Create your views here.

def wish_wall(request):
    if 'logged_user_name' in request.session:
        context = {
            'wishes': Wish.objects.all(),
            'user': User.objects.get(id=request.session['logged_user_id']),
            'users': User.objects.all(),
            'likes': Like.objects.all(),
            'user_likes': Like.objects.filter(wisher=User.objects.get(id=request.session['logged_user_id']))
        }
        return render(request, 'wish_wall.html', context)
    return redirect('/')

def make_wish(request):
    if 'logged_user_name' in request.session:
        return render(request, 'make_wish.html')
    return redirect('/')

def edit_wish(request, wish_id):
    edit_wish = Wish.objects.get(id=wish_id)
    if edit_wish.wisher.id == request.session['logged_user_id']:
        context = {
            'wish': edit_wish
        }
        return render(request, 'edit_wish.html', context)
    return redirect('/wishes/')

def stats(request):
    wishes = Wish.objects.all()
    context = {
        'gw': 0,
        'lu_gw': 0,
        'lu_pw': 0
    }
    for wish in wishes:
        if wish.granted:
            context['gw'] += 1
            if wish.wisher.f_name == request.session['logged_user_name']:
                context['lu_gw'] += 1
        if not wish.granted and wish.wisher.f_name == request.session['logged_user_name']:
            context['lu_pw'] += 1
    return render(request, 'stats.html', context)
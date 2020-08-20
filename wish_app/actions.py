from django.shortcuts import redirect, render
from .models import Wish, Like
from login_app.models import User
import logging

logger = logging.getLogger(__name__)

def create_wish(request):
    if request.method == 'POST':
        Wish.objects.create(
            wish = request.POST['wish'],
            desc = request.POST.get('wish_desc'),
            wisher = User.objects.get(id=request.session['logged_user_id']),
            granted = False
        )
    return redirect('/wishes/')

def remove_wish(request, wish_id):
    rem_wish = Wish.objects.get(id=wish_id)
    if rem_wish.wisher.id == request.session['logged_user_id']:
        rem_wish.delete()
    return redirect('/wishes/')

def edit_wish(request, wish_id):
    if request.method == 'POST':
        edit_wish = Wish.objects.get(id=wish_id)
        if edit_wish.wisher.id == request.session['logged_user_id']:
            edit_wish.wish = request.POST['wish']
            edit_wish.desc = request.POST.get('wish_desc')
            edit_wish.save()
    return redirect('/wishes/')

def grant_wish(request, wish_id):
    grant_wish = Wish.objects.get(id=wish_id)
    if grant_wish.wisher.id == request.session['logged_user_id']:
        grant_wish.granted = True
        grant_wish.save()
    return redirect('/wishes/')

def like_wish(request, wish_id):
    user = User.objects.get(id=request.session['logged_user_id'])
    wish = Wish.objects.get(id=wish_id)
    already_liked = False
    
    for like in wish.likes.all():
        if user.id is like.wisher.id:
            already_liked = True
    if already_liked:
        return redirect('/wishes/')
    else:
        Like.objects.create(
            wish = Wish.objects.get(id=wish_id),
            wisher = User.objects.get(id=request.session['logged_user_id'])
        )
        return redirect('/wishes/')
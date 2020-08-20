from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt, logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return render(request, 'login_reg.html')



def register(request):
    errors = User.objects.reg_validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['pw']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    User.objects.create(
        f_name = request.POST['f_name'],
        l_name = request.POST['l_name'],
        email = request.POST['email'],
        dob = request.POST['dob'],
        password = pw_hash
    )

    lu = User.objects.get(email = request.POST['email'])

    request.session['logged_user_name'], request.session['logged_user_id'] = lu.f_name, lu.id

    return redirect('/wishes/')



def check_email(request):
    context = {
        'found': False
    }

    if len(User.objects.filter(email = request.POST['email'])) > 0:
        context['found'] = True

    return render(request, 'partials/email_found.html', context)



def login(request):
    pw = request.POST['pw']
    user = User.objects.filter(email = request.POST['email'])

    if len(user) > 0 and bcrypt.checkpw(pw.encode(), user[0].password.encode()):
        request.session['logged_user_name'], request.session['logged_user_id'] = user[0].f_name, user[0].id
        return redirect('/wishes/')
    else:
        messages.error(request, 'Email or password is incorrect')
        return redirect('/')



def logout(request):
    request.session.flush()
    return redirect('/')


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
import bcrypt
import datetime

def index(request):
	return render(request, 'login/index.html')

def register(request):
	errors = User.objects.register(request)

	if len(errors) > 0:
		context = {
			'errors': errors
		}
		return render(request, 'login/index.html', context)

	else:
		password = request.POST['password'].encode()
		newpass = bcrypt.hashpw(password, bcrypt.gensalt())
		dbirth = datetime.datetime.strptime(request.POST['dob'], "%Y-%m-%d").strftime('%Y-%m-%d')
		User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=newpass, dob=dbirth)
		request.session['user'] = request.POST['email']
		return redirect(reverse('poke:dashboard'))

def login(request):
	errors = User.objects.login(request)

	if len(errors) > 0:
		context = {
			'errors': errors
		}
		return render(request, 'login/index.html', context)

	else:
		request.session['user'] = request.POST['email']
		return redirect(reverse('poke:dashboard'))
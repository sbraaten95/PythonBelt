from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.db.models import Sum
from ..login.models import User
from .models import Poke, PokeRef

# Create your views here.
def dashboard(request):
	currentUser = User.objects.get(email=request.session['user'])
	context = {
		'self' : currentUser,
		'users' : User.objects.all().exclude(email=request.session['user']),
		'selfcount' : PokeRef.objects.values('poker').distinct().filter(pokeeref=User.objects.get(email=request.session['user'])).count(),
		'eachcount' : PokeRef.objects.filter(pokeeref=currentUser),
		'pokees': Poke.objects.all().exclude(pokee=currentUser).annotate(summed=Sum('count')).order_by('pokee'),
		'notpoked': User.objects.filter(poked=False)
	}
	print context['eachcount']
	return render(request, 'poke/dashboard.html', context)

def poke(request, id):
	try:
		updated = Poke.objects.get(pokee=User.objects.get(id=id))
		updated.count += 1
		updated.save()
	except Poke.DoesNotExist:
		Poke.objects.create(poker=User.objects.get(email=request.session['user']), pokee=User.objects.get(id=id), count=1)
		nowpoked = User.objects.get(id=id)
		nowpoked.poked = True
		nowpoked.save()
	try:
		updated1 = PokeRef.objects.get(poker=User.objects.get(email=request.session['user']), pokeeref=User.objects.get(id=id))
		updated1.count += 1
		updated1.save()
	except PokeRef.DoesNotExist:
		PokeRef.objects.create(poker=User.objects.get(email=request.session['user']), pokeeref=User.objects.get(id=id), count=1)
		nowpoked1 = User.objects.get(id=id)
		nowpoked1.poked = True
		nowpoked1.save()
	return redirect(reverse('poke:dashboard'))

def logout(request):
	request.session.flush()
	return redirect(reverse('login:index'))
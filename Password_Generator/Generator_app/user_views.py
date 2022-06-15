import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from Generator_app.models import PasswordSafe


def IndexView(request):
	if request.method=='GET':
		users = request.session['user_id']
		u=User.objects.get(id=users)
		return render(request,'user/user_index.html',{'user':u})
        # template_name = 'user/user_index.html'

def password(request):
	return render(request, 'user/password_generate.html')

def generator(request):

	if request.method == 'POST':
		users = request.session['user_id']
		u=User.objects.get(id=users)
		print(u,'qqqqqqqqqq')
		user = request.POST['user']
		Password = request.POST['passw']
		creater = PasswordSafe(platform = user, Password= Password)
		creater.user_id=u.id
		creater.save()
		messages.info(request, 'successffully sdded')
		return render(request, 'user/user_index.html')

	else:
		characters = list('abcdefghijklmnopqrstuvwxyz')
		length = int(request.GET.get('length',8))

		if request.GET.get('uppercase'):
			characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

		if request.GET.get('numbers'):
			characters.extend(list('0123456789'))

		if request.GET.get('specialChar'):
			characters.extend(list('!@#$%^&*()+-?<>][}|{'))

		password=''

		for i in range(length):
			password += random.choice(characters)

		print(password)
		return render(request, 'user/generator.html', {'password':password})

def View_Password(request):
        users = request.session['user_id']
        u=User.objects.get(id=users)
        passw =PasswordSafe.objects.filter(id=u.id)
        return render(request, 'user/view_password.html', {'passw':passw})


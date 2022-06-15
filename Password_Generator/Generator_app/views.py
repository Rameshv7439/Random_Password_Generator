import random


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView, View
from Generator_app.models import PasswordSafe, Registration, UserType
from Password_Generator import settings


class IndexView(TemplateView):
    template_name = 'index1.html'

# class Password_Generate(TemplateView):
#     template_name = 'password_generate.html'

def password(request):
	return render(request, 'password_generate.html')
def password2(request):
	return render(request, 'user/password_generate.html')
#
class RegistrationView(TemplateView):
	template_name = 'registration.html'
	def post(self,request,*args,**kwargs):
		name=request.POST['name']
		email=request.POST['email']
		mobile = request.POST['mobile']
		username = request.POST['username']
		password = request.POST['password']
		con_password= request.POST['con_password']
		if password==con_password:
			user=User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='0',last_name='0')
			user.save()
			regs=Registration()
			regs.user= user
			regs.mobile=mobile
			regs.con_password=con_password
			regs.save()
			usertype = UserType()
			usertype.user = user
			usertype.type = "userr"
			usertype.save()
			return render(request,'index1.html',{'message': "Successfully added"})
		else:
			messages = "password does not match"
			return render(request,'registration.html',{'messages':messages})
def generator(request):
	if request.method == 'POST':
		user = request.POST['user']
		Password = request.POST['passw']

		creater = PasswordSafe(platform = user, Password= Password)
		creater.save()
		messages.info(request, 'Your password is saved to the database!!')
		return render(request, 'Thankyou.html')

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
		return render(request, 'generator.html', {'password':password})

def generator1(request):
	if request.method == 'POST':
		user = request.POST['user']
		Password = request.POST['passw']

		creater = PasswordSafe(platform = user, Password= Password)
		creater.save()
		messages.info(request, 'Your password is saved to the database!!')
		return render(request, 'Thankyou.html')

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
		return render(request, 'generator.html', {'password':password})


def View_Password(request):
	if request.method=='GET':
		users = request.session['user_id']
		u=User.objects.get(id=users)
		print(u,'ssss')
		passw =PasswordSafe.objects.filter(user_id=u.id)
		return render(request, 'user/view_password.html', {'passw':passw})
	return render(request, 'user/user_index.html')
class RejectView(View):
	def dispatch(self, request, *args, **kwargs):
		id = request.GET['id']
		print(id,'wwww')
		PasswordSafe.objects.get(id=id).delete()

		return render(request,'user/user_index.html',{'message':"Account Removed"})


# class Login(TemplateView):
#     template_name='login.html'
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         det = User.objects.get(id=1)
#         det.last_name = 1
#         det.save()
#
#         if user is not None:
#
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('/admin')
#             elif UserType.objects.get(user_id=user.id).type == "userr":
#                 request.session['user_id']=user.id
#                 return redirect('/user')
#
#
#         else:
#
#             return render(request, 'login.html', {'message': " User Account Not Authenticated"})



def password1(request):
	return render(request, 'guest_password.html')


def generator1(request):
	# if request.method == 'POST':
	# 	user = request.POST['user']
	# 	Password = request.POST['passw']
    #
	# 	creater = PasswordSafe(platform = user, Password= Password)
	# 	creater.save()
	# 	messages.info(request, 'Your password is saved to the database!!')
	# 	return render(request, 'Thankyou.html')


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
	return render(request, 'generate_password_guest.html', {'password':password})

def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        # det = User.objects.get(id=1)
        # det.last_name = 1
        # det.save()

        if user is not None:

            login(request, user)
            if user.is_superuser:
                return redirect('/admin')
            elif UserType.objects.get(user_id=user.id).type == "userr":
                request.session['user_id']=user.id
                return redirect('/user')


        else:

            return render(request, 'login.html', {'message': " User Account Not Authenticated"})
    else:
        return render(request,'login.html')

def generator2(request):

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

def generator3(request):
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
		return render(request, 'generator.html', {'password':password})

class Forgot_Password(TemplateView):
	template_name = 'forgot_password.html'
	def get_context_data(self, **kwargs):
		context=super(Forgot_Password,self).get_context_data(**kwargs)
		userr=Registration.objects.filter(user__last_name='1').count()
		admin=User.objects.get(is_superuser='1')
		context['userr'] = userr
		context['admin']=admin
		return context
	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		print(username)
		email= request.POST['email']
		print(email)
		user_id=self.request.user.id
		if User.objects.filter(last_name='1',username=username,email=email):
			user=User.objects.get(last_name='1',username=username,email=email)
			Type=UserType.objects.get(user_id=user.id)
			if Type.type=='userr':
				userr=Registration.objects.get(user_id=user.id)
				Password=userr.con_password
				email = EmailMessage(
				Password,
				'Your password',
				settings.EMAIL_HOST_USER,
				[user.email],
				)
				email.fail_silently = False
				email.send()
				return render(request,'index1.html',{'message':"Send mail successfully"})
			else:
				return render(request,'index1.html',{'message':"This User Is Not Exist"})
		else:
			return render(request,'index1.html',{'message':"This User Is Not Exist"})
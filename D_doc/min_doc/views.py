from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic import View

def index(request):
	return HttpResponse("Hello,index")


class Signup(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'register_login/signup.html')

	def post(self, request, *args, **kwargs):
		name = request.POST.get('form-name')
		password1 = request.POST.get('form-password1')
		password2 = request.POST.get('form-password2')
		email = request.POST.get('form-email')
		print('name is:',name,password1,password2,email)
		return HttpResponse("OK")


class Login(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'register_login/login.html')

	def post(self, request, *args, **kwargs):
		pass



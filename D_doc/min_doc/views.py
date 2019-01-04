from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.views.generic import View
from django.contrib.auth.models import User
from .forms import *
from .models import Client, Book
from django.urls import reverse

def index(request):
	return HttpResponse("Hello,index")


class Signup(View):
	template = "register_login/signup.html"
	def get(self, request, *args, **kwargs):
		return render(request, 'register_login/signup.html')

	def post(self, request, *args, **kwargs):
		form = SignUpForm(request.POST)
		if form.is_valid():
			print("form is :",form)
			name = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			if password1 != password2:
				return HttpResponse("Password don't match")
			else:
				client = Client(username=name,password=password1,email=email)
				client.save()
				return redirect(reverse('login'))
		else:
			return render(request,self.template,{'form':form})


class Login(View):
	template = 'register_login/login.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template)

	def post(self, request, *args, **kwargs):
		print("post")
		form = LogInForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				client = Client.objects.get(username=name)
				if client.password != password:
					return HttpResponse("Password error")
				else:
					uuid = client.uuid
					print("uuid is :",uuid)
					return redirect(reverse('book_list', kwargs={'uuid': uuid}))
			except:
				return HttpResponse("The User does not exist!")
		else:
			print("errrors:",form.errors)
			return render(request, self.template, {'form': form})


class BookList(View):
	template = 'book/book_list.html'
	def get(self,request, *args, **kwargs):
		client_uuid = self.kwargs.get('uuid')
		client = Client.objects.get(uuid=client_uuid)
		books = Book.objects.filter(user=client)
		print("books is:",books,len(books))
		return render(request, self.template, {'books': books})


class BookOverView(View):
	pass


class BookEditor(View):
	pass

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greeting(request):
	name = request.GET['name']
	message = request.GET['message']

	response = f'Hello, {name}!\n{message}!'
	return render(request, 'greeting/greeting.html', 
		{'name': name, 
		 'message': message}
		)

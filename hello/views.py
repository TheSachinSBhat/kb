from django.shortcuts import render
from django.http import HttpResponse

import json

from django.core import serializers

from django.db import models
from .models import Greeting

# Create your views here.
def index(request):
	# return HttpResponse('Hello from Python!')
	return render(request, 'index.html')

def api(request):
	#some_data_to_dump = {
	#	'some_var_1': 'foo',
	#	'some_var_2': 'bar',
	#}

	#data = json.dumps(some_data_to_dump)

	class Person(models.Model):
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)

	sachin = Person()
	sachin.first_name = 'Sachin'
	sachin.last_name = 'Bhat'

	persons = set([])

	persons.add(sachin)

	data = serializers.serialize('json', persons)

	return HttpResponse(data, content_type='application/json')

	#return HttpResponse('Hello from KB IO API!')

def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})


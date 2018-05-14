from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import Question


# Create your views here.
def  index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list
	}
	# return render(request, 'polls/index.html',context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk= question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
		return render(request,'polls/detail.html',{'question':question})

	#return HttpResponse ("Usted esta buscando una pregunta %s." %question_id)

def results (request, question_id):
	response = "Usted esta buscando un resultado a una respuesta %s."
	return HttpResponse(response % question_id)
def vote (request, question_id):
	return HttpResponse("Usted a votado %s." %question_id)
	#http://www.mediafire.com/convkey/853e/9n4feppccbuq0bjzg.jpg

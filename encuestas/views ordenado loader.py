from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:18]
#1    output = ', '.join([q.question_text for q in latest_question_list])
#1    return HttpResponse(output)
#0     return HttpResponse("Indice de Encuestas by BB")
    template = loader.get_template('encuestas/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Está buscando la pregunta %s." % question_id)

def results(request, question_id):
    response = "Buscando el resultado de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Está respondiendo la pregunta %s." % question_id)

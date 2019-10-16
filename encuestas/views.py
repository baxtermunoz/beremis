
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#from django.http import  HttpResponseRedirect
#2from django.template import loader
#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import datetime
#=======================================
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last six published questions."""
        return Question.objects.order_by('-pub_date')[:18]
		
class DetailView(generic.DetailView):
    model = Question
    template_name = 'encuestas/detail.html'
		
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'encuestas/results.html'
		

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:18]
#1    output = ', '.join([q.question_text for q in latest_question_list])
#1    return HttpResponse(output)
#0     return HttpResponse("Indice de Encuestas by BB")
#2   template = loader.get_template('encuestas/index.html')
#2   context = {
#2       'latest_question_list': latest_question_list,
#2   }
#2   return HttpResponse(template.render(context, request))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'encuestas/index.html', context)


def detail(request, question_id):
#3    try:
#3        question = Question.objects.get(pk=question_id)
#3    except Question.DoesNotExist:
#3        raise Http404("Preguntas no existe")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/detail.html', {'question': question})
#0    return HttpResponse("Está buscando la pregunta %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/results.html', {'question': question})
#    response = "Buscando el resultado de la pregunta %s."
#    return HttpResponse(response % question_id)

def vote(request, question_id):
#    return HttpResponse("Está respondiendo la pregunta %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'encuestas/detail.html', {
            'question': question,
            'error_message': "No hizo una selección.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('encuestas:results', args=(question.id,)))
		
#def fechayhora_actual (request)
#    now = datetime.datetime.now()
#    html = "<html><body>Fecha %s.</body></html>" % now
#    return HttpResponse(html)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
import datetime
import logging
logger = logging.getLogger(__name__)

from .models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        logdata(question_id, selected_choice, request.session)
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being posted twice if a
        #user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def logdata(question_id, choice, session):
    session.modified=True
    logger.info(str(datetime.datetime.now())[:19]+"-"+str(session.session_key)+"-"+str(question_id)+"-"+str(choice))

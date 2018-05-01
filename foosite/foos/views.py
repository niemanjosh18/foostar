from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Player
from .models import Question

def index(request):
    recent_qs = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('foos/index.html')
    context = { 
        'recent_qs': recent_qs,
    }
    return HttpResponse(template.render(context,request))

# another way to write index...
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
         raise Http404("Question does not exist")
    return render(request, 'foos/detail.html', {'question': question})

# here is a better way to write detail...
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def player(request, player_id):
    return HttpResponse("You are looking at player %s." % player_id)

def singles(request):
    top_10_singles = Player.objects.order_by('-ratingS')[:10]
    template = loader.get_template('foos/singles.html')
    context = {
        'top_10_singles': top_10_singles,
    } 
    return HttpResponse(template.render(context,request))

def doubles(request):
    top_10_doubles = Player.objects.order_by('-ratingD')[:10]
    template = loader.get_template('foos/doubles.html')
    context = {
        'top_10_doubles': top_10_doubles
    }
    return HttpResponse(template.render(context,request))



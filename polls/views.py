from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic


# Create your views here.
"""
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    #response = ', '.join([q.question_text for q in question_list])
    template = loader.get_template('polls/index.html')
    context = {'question_list' : question_list}
    return HttpResponse(template.render(context,request))


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
        #choice = question.choice_set.all()
        #choice = zip(range(len(choice)),choice) #adding a counter
    except Question.DoesNotExist:
        raise Http404("Page does not exist")
    context = {'question': question}
    return render(request, 'polls/details.html', context)
    #return HttpResponse("You are viewing the details of Question: %s" % question_id)


def results(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request,'polls/results.html', {'question':question})
"""

#Using Generic Views
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Page does not exist")

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/details.html',{'question':question,'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args={question.id}))

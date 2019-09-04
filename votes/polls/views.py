from django.shortcuts import render

from .models import Question,Choice

#get questions and display 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html', context)


#show specific question and choices 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/deatil.html', {'question':question})

# Get question and display result 
def results(request, question_id):
    question = get_object_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
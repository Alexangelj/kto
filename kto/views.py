from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice, Task
from .forms import TaskForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'kto/index.html'
    context_object_name = 'task_list_name'

    def get_queryset(self):
        return Task.objects.order_by('-priority')[:5]

class DetailView(generic.DetailView):
    model = Task
    template_name = 'kto/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'kto/results.html'
    
def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            Task.objects.create_task(task)
            all_tasks = Task.objects.all
            messages.success(request, ('Task Added'))
            return HttpResponseRedirect(reverse('kto:index'))
    else:
        task = TaskForm()
    

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.success(request, ('Task Deleted'))
    return HttpResponseRedirect(reverse('kto:index'))
"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'kto/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('kto:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'kto/results.html', {'question': question})
"""
"""
def add_task(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valied():
            form.save()
            items = Task.objects.all
            messages.success(request, ('Task added.'))
"""




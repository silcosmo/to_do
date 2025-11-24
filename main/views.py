from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from main.models import Task #importar a tabela que se quer usar

class HomeView(TemplateView):
    template_name = 'home.html'

class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'

#criando uma vier
def task_list(request):
    tarefas = Task.objects.all() #trazendo tudo da tabela tarefas
    context ={
        "tarefas": tarefas,
        "titulos_pagina": 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)

def task_concluido(request):
    a=4
    b=5
    c= a+b

    tarefas =Task.objects.filter(concluida=1)
    context = {
        "tarefas":tarefas,
        "titulo_pagina": "Minhas Tarefas Concluidas",
        'c':c    
        }
    return render(request, 'tasks/concluidas.html', context)


  
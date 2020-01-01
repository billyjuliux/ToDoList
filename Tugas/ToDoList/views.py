from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request) :
    allItems = TodoItem.objects.all()
    return render(request, 'todoView.html' , {'all_items' : allItems} , {'editNum' : -1})

def addTodo(request) :
    TodoItem(content = request.POST['content']).save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request , todo_id) : 
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo/')

def editTodo(request , todo_id) :
    TodoItem.objects.get(id=todo_id).content = "Input new content then click 'Add'."
    return render(request, 'todoView.html' , {'all_items' : allItems} , {'editNum' : todo_id})

def editTodoChange(request , editNum) :
    TodoItem.objects.get(id=editNum).content = request.POST['content']
    TodoItem.objects.get(id=editNum).save()
    return HttpResponseRedirect('/todo/')
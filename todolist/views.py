from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Index View
def index(request):
    todo_items = Todolist.objects.order_by('id')  # Fetch all todo items
    form = TodoListForm()  # Initialize an empty form
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)

# Add Todo Item View
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)  # Bind form with POST data

    if form.is_valid():  # Validate the form
        text = form.cleaned_data['text']  # Get cleaned data
        Todolist.objects.create(text=text, completed=False)  # Save to database
        print(f"Added todo: {text}")  # Debugging statement

    return redirect('index')  # Redirect to the index page


def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact = True).delete()

    return redirect('index')


def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')




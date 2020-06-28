from django.shortcuts import render, redirect
from .models import TodoListItem
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
from django.utils import timezone



# Normal View of the webpage
def todoappView(request):
    if request.method == 'POST':
        context = {}
        dates = request.POST['dates']
        print(dates)
        all_items = TodoListItem.objects.filter(date = dates)
        date = datetime.datetime.now()
        formated_date = date.strftime("%Y-%m-%d")
        all_todo_items = TodoListItem.objects.all().order_by('date')
        pending = []
        future = []
        for item in all_todo_items:
            d = datetime.datetime(item.date.year,item.date.month,item.date.day,0,0,0,0,None)
            if d > date:
                future.append(item)
            elif d < date:
                if d.day != date.day:
                    pending.append(item)
        context['all_items'] = all_items
        context['today'] = formated_date
        context['items'] = pending
        context['future'] = future
        context['dates'] = dates
        return render(request, 'todolist.html',context)
    else:
        context = {}
        date = datetime.datetime.now()
        formated_date = date.strftime("%Y-%m-%d")
        yesterday = date - datetime.timedelta(days=1)
        formated_yest = yesterday.strftime("%Y-%m-%d")
        yest_items = TodoListItem.objects.filter(date = formated_yest)
        for i in yest_items:
            i.future = False
            i.save()
        all_items = TodoListItem.objects.filter(date = formated_date)
        all_todo_items = TodoListItem.objects.all().order_by('date')
        pending = []
        future = []
        for item in all_todo_items:
            d = datetime.datetime(item.date.year,item.date.month,item.date.day,0,0,0,0,None)
            if d > date:
                future.append(item)
            elif d < date:
                if d.day != date.day:
                    pending.append(item)
        context['all_items'] = all_items
        context['today'] = formated_date
        context['items'] = pending
        context['future'] = future
        return render(request,'todolist.html',context)


# Adding Items
def addTodoView(request):
    x = request.POST['content']
    date = datetime.datetime.now()
    formated_date = date.strftime("%Y-%m-%d")
    if x == '':
        return HttpResponseRedirect('/')
    new_item = TodoListItem(item=x, date=formated_date)
    new_item.save()
    messages.success(request,('Item has been Added!!'))
    return HttpResponseRedirect('/')


def addFutureTask(request):
    x = request.POST['task']
    date = request.POST['date']
    if x == '':
        return HttpResponseRedirect('/')
    new_item = TodoListItem(item = x, date = date)
    new_item.save()
    messages.success(request, ('Item has been Recorded!!'))
    return HttpResponseRedirect('/')


# Deleting Items
def deleteTodoView(request,i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    messages.success(request, ('Item has been Deleted!!'))
    return HttpResponseRedirect('/')


# Setting the item as completed
def cross_off(request,i):
    item = TodoListItem.objects.get(id = i)
    item.completed = True
    item.save()
    return redirect('home')


# Setting the item as not completed
def uncross(request,i):
    item = TodoListItem.objects.get(id = i)
    item.completed = False
    item.save()
    return redirect('home')


# to edit the item name
def edit(request,i):
    if request.method == 'POST':
        item = TodoListItem.objects.get(id = i)

        x = request.POST['content']
        item.item = x
        item.save()
        messages.success(request,('Item has been edited!!'))
        return redirect('home')

    else:
        item = TodoListItem.objects.get(id = i)
        return render(request, 'edit.html', {'item':item})
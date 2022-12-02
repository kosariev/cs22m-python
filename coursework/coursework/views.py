from django.shortcuts import render, redirect
from coursework.models import Cars
from coursework.forms import CarsForm


def index(request):
    return render(request, 'index.html', {'title': 'Головна сторінка', 'page': 'index'})


def cars(request):
    return render(request, 'cars.html', {'title': 'Перелік', 'page': 'cars', 'cars': Cars.objects.all()})


def add(request):
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars')
    else:
        form = CarsForm()
    return render(request, 'add.html', {'title': 'Додати авто', 'page': 'cars', 'form': form})


def edit(request, car_id):
    car = Cars.objects.get(id=car_id)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("/cars")
    form = CarsForm(instance=car)
    return render(request, 'edit.html', {'title': 'Редагувати авто', 'page': 'cars', 'car': form})


def update(request, car_id):
    car = Cars.objects.get(id=car_id)
    form = CarsForm(request.POST, instance=car)
    if form.is_valid():
        form.save()
        return redirect("/cars")
    return render(request, 'edit.html', {'car': car})


def destroy(request, car_id):
    car = Cars.objects.get(id=car_id)
    car.delete()
    return redirect("/cars")

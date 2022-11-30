from django.http import HttpResponse
from django.shortcuts import render, redirect
import joblib
from .form import *
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
import pickle


# def home(request):
#     return render(request, "login.html")


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    return render(request, "register.html", {'form': form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        us = request.POST['username']
        ps = request.POST['password']
        if us is not None and ps is not None:
            user = authenticate(request, username=us, password=ps)
            if user:
                login(request, user)
                return redirect('dises')
    return render(request, 'login.html', {'form': form})


def get_output(list_data):
    model = joblib.load("app/model.sav")
    prediction = model.predict([list_data])
    return prediction


def dises(request):
    form = DiseasesForm()
    if request.method == "POST":
        form = DiseasesForm(request.POST)
        if form.is_valid():
            form.save()
            age = form.cleaned_data['age']
            pain_type = form.cleaned_data['pain_type']
            blood_pressure = form.cleaned_data['blood_pressure']
            cholesterol = form.cleaned_data['cholesterol']
            blood_sugar = form.cleaned_data['blood_sugar']
            ecg = form.cleaned_data['ecg']
            hart_rate = form.cleaned_data['hart_rate']
            exang = form.cleaned_data['exang']
            old_peak = form.cleaned_data['old_peak']
            slope = form.cleaned_data['slope']
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']
            male = form.cleaned_data['male']
            female = form.cleaned_data['female']
            sex = ''
            if male == 'on':
                sex = str(1)
            else:
                sex = str(1)

            list_data = [age, sex, pain_type, blood_pressure, cholesterol, blood_sugar, hart_rate, ecg,exang,
                          old_peak, slope, ca, thal
                         ]
            data = get_output(list_data)
            output = ''
            if data[0] == 0:
                output = 'result'
            else:
                output = 'results'
            return redirect('output', output)
    return render(request, "dises.html", {'form': form})


def output(request, rs):
    result = ''
    if rs == 'result':
        result = 0
    elif rs == 'results':
        result = 1

    return render(request, "output.html",{'result':result})

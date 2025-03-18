from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages  # messages import qilish kerak
from django.utils.translation.template import context_re

from .forms import *

def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(request, phone_number=phone_number, password=password)

        if user is not None:
            login(request, user)

            if user.is_admin:
                return redirect("admin_panel")  # Admin sahifasi
            if user.is_staff:
                return redirect("staff_panel")  # Foydalanuvchi sahifasi
        else:
            messages.error(request, "Telefon raqam yoki parol noto‘g‘ri")

    # else:
    #     form=UserLoginForm()
    context={
        'form':UserLoginForm
    }
    return render(request, "login.html" ,context=context)


def admin_panel(request):
    context={
        "data":"Adminkaga hush kelibsiz"
    }
    return render(request  , 'admin_panel.html',context=context)


def staff_panel(request):
    return render(request  , 'staff_panel.html')



def add_students(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = form.save()
            return redirect('home')
    else:
        form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


def add_teachers(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = form.save()
            return redirect('home')
    else:
        form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


def index(request):
    students=Student.objects.all()
    teachers=Teacher.objects.all()
    context={
        'students':students,
        'teachers':teachers,
    }
    return render(request,'index.html',context=context)

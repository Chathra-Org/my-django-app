from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        if first_name and last_name and email:
            try:
                Registration.objects.create(first_name=first_name, last_name=last_name, email=email)
                messages.success(request, "Registration successful!")
                return redirect("register")
            except Exception as e:
                if "UNIQUE constraint failed" in str(e):
                    messages.error(request, "A user with this email already exists")
                else:
                    messages.error(request, "An error occurred during registration")
    return render(request, "register.html")

def registrations(request):
    regs = Registration.objects.all().order_by('-registered_at')
    return render(request, 'registrations.html', {'registrations': regs})
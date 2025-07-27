from django.shortcuts import render
from .models import Registration

def register(request):
    message = None
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        if first_name and last_name and email:
            Registration.objects.create(first_name=first_name, last_name=last_name, email=email)
            message = "Registration successful!"
    return render(request, "register.html", {"message": message})

def registrations(request):
    regs = Registration.objects.all().order_by('-registered_at')
    return render(request, 'registrations.html', {'registrations': regs})

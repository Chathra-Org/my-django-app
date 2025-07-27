from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Registration

def register(request):
    errors = {}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if not first_name:
            errors["first_name"] = "This field is required."
        if not last_name:
            errors["last_name"] = "This field is required."
        if not email:
            errors["email"] = "This field is required."
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = "Enter a valid email address."
            else:
                if Registration.objects.filter(email=email).exists():
                    errors["email"] = "A user with this email address already exists."

        if not errors:
            Registration.objects.create(first_name=first_name, last_name=last_name, email=email)
            return redirect("register_success")

    return render(request, "register.html", {"errors": errors})

def register_success(request):
    return render(request, "register_success.html", {"message": "Registration successful!"})

def registrations(request):
    regs = Registration.objects.all().order_by('-registered_at')
    return render(request, 'registrations.html', {'registrations': regs})
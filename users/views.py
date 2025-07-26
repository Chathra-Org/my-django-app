# users/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            # If username is not provided, return an error
            if not username:
                return JsonResponse({"error": "Missing username"}, status=400)
            email = data.get("email")
            if not username or not email:
                return JsonResponse({"error": "Missing username or email"}, status=400)
            return JsonResponse({"message": f"User {username} created", "email": email}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

#write update user method
@csrf_exempt
def update_user(request, username):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            if not email:
                return JsonResponse({"error": "Missing email"}, status=400)
            return JsonResponse({"message": f"User {username} updated", "email": email}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

#write delete user method
@csrf_exempt
def delete_user(request, username):
    if request.method == "DELETE":
        # Here you would typically delete the user from the database
        return JsonResponse({"message": f"User {username} deleted"}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)

#write list users method
@csrf_exempt
def list_users(request):
    if request.method == "GET":
        return JsonResponse({"users": ["user1", "user2", "user3"]}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)

#write get user method
@csrf_exempt
def get_user(request, username):
    if request.method == "GET":
        # Here you would typically fetch the user from the database
        return JsonResponse({"username": username, "email": f"{ username }@example.com"}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)    
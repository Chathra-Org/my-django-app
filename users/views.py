# users/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def users_collection(request):
    if request.method == "GET":
        # List users
        return JsonResponse({"users": ["user1", "user2", "user3"]}, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
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
def user_detail(request, username):
    if request.method == "GET":
        # Get user
        return JsonResponse({"username": username, "email": f"{username}@example.com"}, status=200)
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            if not email:
                return JsonResponse({"error": "Missing email"}, status=400)
            return JsonResponse({"message": f"User {username} updated", "email": email}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    elif request.method == "DELETE":
        return JsonResponse({"message": f"User {username} deleted"}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)

#write delete user method

# The following views are now handled by users_collection and user_detail
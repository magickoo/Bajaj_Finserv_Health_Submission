from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'bfhl/index.html')

@csrf_exempt
def bfhl_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))['data']
            user_id = "your_fullname_ddmmyyyy"
            email = "your_email@example.com"
            roll_number = "21BRS1529"

            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            lowercase_alphabets = [char for char in alphabets if char.islower()]
            highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"is_success": False, "error": str(e)}, status=400)

def bfhl_get(request):
    if request.method == 'GET':
        return JsonResponse({"operation_code": 1})

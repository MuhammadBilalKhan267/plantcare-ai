from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import numpy as np
import io
from .detect import detect_disease
from .chat import diagnose


# Create your views here.
def home(request):
    return render(request, "home.html")

def detect(request):
    return render(request, "detect.html")

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        # Read the file into memory and convert it to a NumPy array
        image_pil = Image.open(io.BytesIO(image_file.read()))  # Open as PIL Image
        image_np = np.array(image_pil, dtype="uint8")  # Convert to NumPy array

        results = detect_disease(image_np)
        name = results[0][0]

        description = diagnose(name)

        return JsonResponse({
            "message": "File processed successfully",
            "name": name,
            "description": description,
        })
    
    return JsonResponse({"error": "Invalid request"}, status=400)

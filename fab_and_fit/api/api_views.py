# api/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# from .services.food_analysis import analyze_food_image, analyze_meal_text
from .services.food_anaiysis import analyze_food_image, analyze_meal_text
class FoodAnalysisView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        # Check if an image was uploaded or a text meal description was provided
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            result = analyze_food_image(image_file.read())
        else:
            meal_text = request.data.get('meal_text', '')
            result = analyze_meal_text(meal_text)
        return Response(result)

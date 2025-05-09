# api/api_routes.py
from django.urls import path
from .api_views import FoodAnalysisView, MealPlanView

urlpatterns = [
    path('food/analyze/', FoodAnalysisView.as_view(), name='food-analyze'),
    path('mealplan/', MealPlanView.as_view(), name='meal-plan'),
]

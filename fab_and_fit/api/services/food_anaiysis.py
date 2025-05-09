# api/services/food_analysis.py
import logging
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential


logger = logging.getLogger(__name__)
model = genai.GenerativeModel('gemini-pro-vision')

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def analyze_food_image(image_bytes):
    """Call Gemini vision API with the image and parse the response."""
    try:
        response = model.generate_content([None, image_bytes, "Identify and list the ingredients with quantities."])
        return response
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        raise

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def analyze_meal_text(meal_text):
    """Call Gemini API with the text description of a meal and parse the response."""
    try:
        prompt = f"Analyze this meal description: '{meal_text}'. Identify and list the ingredients with quantities."
        response = model.generate_content(prompt)
        return response
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        raise

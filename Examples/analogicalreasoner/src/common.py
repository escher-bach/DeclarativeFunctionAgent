import os
import google.generativeai as genai
import json
from google.ai.generativelanguage_v1beta.types import content

# Configure Gemini API globally
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)

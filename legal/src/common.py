import os
import google.generativeai as genai
import json
from google.ai.generativelanguage_v1beta.types import content

# Configure Gemini API globally
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)

# Common configurations for legal document processing
DEFAULT_GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}

# Export everything needed by other modules
__all__ = ['os', 'genai', 'json', 'content']

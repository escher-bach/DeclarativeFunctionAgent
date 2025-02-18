import os
from src.common import genai, content, json

# Import implemented functions
from src.generate_joke import generate_joke

# Original implementation
def joke(topic):
 x = generate_joke(topic)
 print(x)

joke("dogs and the world")
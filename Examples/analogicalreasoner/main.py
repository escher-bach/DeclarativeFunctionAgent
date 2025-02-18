import os
from src.common import genai, content, json

# Import implemented functions
from src.find_correspondences import find_correspondences
from src.transfer_knowledge import transfer_knowledge

# Original implementation
def analogical_reasoner(source, target): #both strings
 mapping = find_correspondences(source, target) #uses api to find commonalities
 adapted_knowledge = transfer_knowledge(source, mapping) #returns knowledge in the form of text
 return adapted_knowledge

print(analogical_reasoner("Postmordernism","Wittgenstein"))
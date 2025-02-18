import os
from src.common import genai, content, json

# Import implemented functions
from src.satisfied import satisfied
from src.antithesis import antithesis
from src.synthesis import synthesis

# Original implementation
def dialectic_reasoner(x):
 thesis = x
 while not satisfied(thesis):
  syn = synthesis(thesis,antithesis(thesis))
  thesis = syn
 return thesis
x = input("What do you want to reason about? ")
print(dialectic_reasoner(x))
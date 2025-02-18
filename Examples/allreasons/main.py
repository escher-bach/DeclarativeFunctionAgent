import os
from src.common import genai, content, json

# Import implemented functions
from src.explains import explains
from src.find_patterns import find_patterns
from src.generalize import generalize
from src.is_most_plausible import is_most_plausible
from src.antithesis import antithesis
from src.satisfied import satisfied
from src.synthesis import synthesis

# Code from project 1

# Import implemented functions

# Original implementation
def inductive_reasoner(observations): #takes in string and returns a string
 patterns = find_patterns(observations) # returns a string that takes in pattern uses api as needs common sense to find patterns 
 hypothesis = generalize(patterns) # same as above uses common sense so needs api
 return hypothesis


def abductive_reasoner(observations, hypotheses):
 best_explanation = None
 for h in hypotheses:
  if explains(h, observations) and is_most_plausible(h): #again work on strings not numbers so need common sense
   best_explanation = h
 return best_explanation

print(explains(inductive_reasoner("""
                   "2, 4, 6 follows the rule",  
                "3, 6, 9 follows the rule",  
                "5, 10, 15 follows the rule"""),"9,18,27")) #TRUE

print(explains(inductive_reasoner("""
                   "2, 4, 6 follows the rule",  
                "3, 6, 9 follows the rule",  
                "5, 10, 15 follows the rule"""),"9,9,27")) #FALSE



# Code from project 2

# Import implemented functions

# Original implementation
def dialectic_reasoner(x):
 thesis = x
 while not satisfied(thesis):
  syn = synthesis(thesis,antithesis(thesis))
  thesis = syn
 return thesis
x = input("What do you want to reason about? ")
print(dialectic_reasoner(x))

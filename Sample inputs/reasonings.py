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

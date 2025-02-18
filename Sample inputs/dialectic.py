def dialectic_reasoner(x):
 thesis = x
 while not satisfied(thesis):
  syn = synthesis(thesis,antithesis(thesis))
  thesis = syn
 return thesis
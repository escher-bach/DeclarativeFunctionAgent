def analogical_reasoner(source, target): #both strings
 mapping = find_correspondences(source, target) #uses api to find commonalities
 adapted_knowledge = transfer_knowledge(source, mapping) #returns knowledge in the form of text
 return adapted_knowledge
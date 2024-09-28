tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)

#indexing 
print(tea_varieties[0]) #for first index
print(tea_varieties[1]) #for second index
print(tea_varieties[-1]) #if we want to start from last
print(tea_varieties[1:3]) #if we want 2nd and 3rd index
print(tea_varieties[:2]) #if we want first two index

#List manipulation
tea_varieties[3] = "Herbal" 
print(tea_varieties)
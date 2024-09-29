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

for tea in tea_varieties:
    print(tea)

if "White" in tea_varieties:
    print("I have White Tea")
else:
    print("Append it Bro")

tea_varieties.append("White") #Append on a array
print(tea_varieties)

tea_varieties.append("Lemon")
print(tea_varieties)

# If we want to remove the last element in the list
tea_varieties.pop()
print(tea_varieties)

tea_varieties.append("Tulshi")#Append on a array
print(tea_varieties)

#If we want to remove any item by name
tea_varieties.remove("Tulshi")
print(tea_varieties)

# If We Want to insert a item on my comfortable position
tea_varieties.insert(1,"Lemon Grass")
print(tea_varieties)

# If We want to copy an array to another variable 
tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy)


squared_num = [x**2 for x in range(10)]
print(squared_num)

cube_num = [x**3 for x in range(10)]
print(cube_num)
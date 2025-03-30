# A set only romove the unique element of the set

a1 = {3, 5, 23, 5, 5, 5}
a2 = {3, 5, 23, 7, 8, 0}

print(a1.pop()) #randomly remove an element from the set

a1.add(2)
print(a1)

print(a1.intersection(a2)) # intersection means the common elements from the both sets

print(a1.union(a2)) # union means all elements from both sets but identical




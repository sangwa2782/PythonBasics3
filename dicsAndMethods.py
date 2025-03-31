a = {} # represent Dict type
b = set() # represent set type

print(a, type(a))
print(b, type(b))

marks = {"Harshit": 34, "Harry": 99, "Shivani": 8, "Smriti": 45, "Naina": 78, "Sankalp": 78}

print(marks["Harry"])

marks["Krishna"] = 100
print(marks["Krishna"])

print(marks.get("Krishna Arya")) #.get blocks error and returns None

print(marks.keys()) # shows key values
print(marks.values()) # shows the values of the keys
print(marks.items()) # shows the keys and values in brackets

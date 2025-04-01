s = "Harry is a good boy 2"
# Writing to a file (there is two code, and both you can use)
#writing a file
# with open("ajay.txt", "w") as f:
#     f.write(s)

# writing a file
fp = open("ajay.txt", "w")
fp.write(s)
fp.close()

# reading to a file
# with open("ajay.txt", "r") as f:
#     s = f.read()
#     print(s)

# reading a file
f = open("ajay.txt", "r")
s = f.read()
print(s)
f.close()
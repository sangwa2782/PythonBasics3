def greetHello(name, ending):
    print("Hello " + name)
    print("Hello")
    print("Hello")
    print(ending)

#function with text
def letterGenerator(name, date):
    st = f"Hi mam, \nThis is {name} and I will not come to school on {date}."
    print(st)

#functions with return
def average(a, b):
    return (a+b)/2

print("Excuting function...")
greetHello("Ajay", "Thankyou")
letterGenerator("Ajay", "2 April 2025")
print(average(8,6))
print("done")

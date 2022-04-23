def add (a, b = 5):
    return a + b
 
x = add(2,3)
print(x) 
 
y = add(7)
print(y) 
 
total = add(x,y)
print(total)




def add (a, b):
    return a + b
 
x = add(a = 2, b =3)
print(x)
 
y = add(b = 7, a=11)
print(y)
 
total = add(b=x,a=y)
print(total)




c = 5
def add (a, b):
    c = a + b
    return c
 
# will get an exception
x = add(12, 23)
print(x)
 
# use global
 
def add (a, b):
    global c
    c = a + b
    return c



# multiple return

def get_a_lot(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y1
    return (y0, y1, y2)
 
things = get_a_lot(5)





# Define `main()` function
def main():
 hello()
 print("This is the main function")


# Execute `main()` function
if __name__ == '__main__':
   main()




def add_everything(*args):
    return sum(args)
 
# Calculate the sum
print(add_everything(1,4,5, 75, 112))







c = 5
def add (a, b):
    c = a + b
    return c
 
# will get an exception
x = add(12, 23)
print(x)
 
# use global
 
def add (a, b):
    global c
    c = a + b
    return c
def add (a, b):
    return a + b
    
    
    
 
x = add(a = 2, b =3)
print(x)
 
y = add(b = 7, a=11)
print(y)
 
total = add(b=x,a=y)
print(total)





double = lambda x: x * 2
# Output: 10
print(double(5))










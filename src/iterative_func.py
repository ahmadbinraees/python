def factorial(num):
   fact = 1
   while num > 0:
      fact = fact * num
      num = num -1
   return fact

print(factorial(4))




def factorial (n):
   if n <= 1 :
      return 1
   else:
      return n * factorial(n-1)

print(factorial(5))






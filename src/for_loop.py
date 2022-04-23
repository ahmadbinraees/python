nums = [12, 54, -21, 113]
for num in nums:
   if num > 0:
     print(num)


nums = [12, 54, -21, 113, 35]
for num in nums:
   if num < 0:
     break
   print(num)


nums = [1, 22, 35, -21, 45, 16, 18]
for num in nums:
   if num % 2 == 0:
      continue
   print(num)


#this logic will ignore the negative nums

nums = [1, 22, -3, -21, -45, 35, -18]
for num in nums:
   if num < 0:
      continue
   print(num)






     




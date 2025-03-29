import sys
'''
#Printing numbers from 1 to 10
for num in range(1,11):
    print(num)

#Printing numbers from 1 to 20 . only even

for num in range(1,21):
    if num % 2 == 0:
        print(num)

    else:
        continue

#Find the Sum of first natural numbers

sum = 0
for detail in range(1,101):
    print(detail)
    sum+= detail

print(sum)


name ='shalini'
rev =''
for letter in name:
    rev = letter + rev
    #print(letter)
print(rev)


#printing patters using nested for loops

'''
n= 10

for i in range(1, n+1):
  for j in range(i):
     print("*",end='')
  print()
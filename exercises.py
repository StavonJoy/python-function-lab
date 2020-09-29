# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.


def sum_to(n):
  return sum(range(n + 1))
  
print(sum_to(5))


# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.


def largest(li):
  return max(li)

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))


# 3. Write a function named `occurances` that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurences(str1, str2):
  return str1.count(str2)


print(occurences('fleep floop', 'e'))  
print(occurences('fleep floop', 'p')) 
print(occurences('fleep floop', 'ee')) 
print(occurences('fleep floop', 'fe')) 


# 4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product.<br>(HINT: Review your notes on `*args`).

def product(*args):
  product = 1
  for a in args:
    product *= a
  return product



print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0

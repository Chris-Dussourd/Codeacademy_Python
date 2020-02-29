

# Sum the digits in the number (Ex: 6784 input, 6+7+8+4=25)
def digit_sum(n):
  total=0
  while n>0:
    total+=n%10
    n=(n-n%10)/10
  return total

print(digit_sum(38957))

# Returns the factorial of a number
def factorial(x):
  fact=1
  for i in range(2,x+1):
    fact=fact*i
  return fact
    
print(factorial(5))

# Find if a number is aprime number
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(11))


# Returns the score of a word in scrabble (excluding double/triple bonuses)
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        for leter in score:
            if letter == leter:
                total = total + score[leter]
    return total

print(scrabble_score("Zero"))


# If word is found in text, replace it with the asterisks (number of asterisks=length of word)
def censor(text,word):
  asterisks="*"*len(word)
  text_array=text.split(word)
  return asterisks.join(text_array)

print(censor("what the duck is that","duck"))


# Count the number of times item appears in sequence
def count(sequence,item):
  num=0
  for i in sequence:
    if item==i:
      num=num+1
  return num

print(count([1,2,1,1],1))


# Removes all the odd numbers in a list.
def purify(numbers):
  new_list=[]
  for i in numbers:
    if i%2==0:
      new_list.append(i)
  return new_list

print(purify([5,8,6,4,9,10]))


# Finds the product of all the numbers in a list
def product(integers):
  prod=1
  for i in integers:
    prod=prod*i
  return prod

print(product([5,4,0]))

# Remove the duplicates in an array of numbers
test=[4,5,5,4]
print(remove_duplicates(test))
print(test)

def remove_duplicates(numbers):
  new_list=[]
  for i in numbers:
    if i not in new_list:
      new_list.append(i)
  return new_list

test=[5,5,3,7,3,7,8]
print(remove_duplicates(test))
print(test)


# Find the median of an array of numbers
def median(numbers):
  new_list=[]
  new_list.extend(numbers)
  new_list.sort()
  length=len(new_list)
  if length%2==0:
    return (new_list[int(length/2-1)]+new_list[int(length/2)])/2.0
  else:
    return new_list[int(length/2.0-.5)]
  
print(median([6,8,12,2,23]))
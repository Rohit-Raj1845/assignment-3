QUESTION:-1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
def keyword is used to create a function.
def odd_numbers(n): 
    return [x for x in range(n+1) if x % 2 != 0]
print(odd_numbers(25))



QUESTION:-2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
When you are unsure about the number of arguments to pass in the functions.
def adder(*num): 
    sum = 0
    for n in num: 
        sum = sum + n
    print("sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data): 
    print("\nData type of argument:",type(data))
    for key, value in data.items(): 
        print("{} : {}". format(key,value))
intro(Firstname = "Rohit", Lastname = "Raj", Age = 20, Email = "rohitraj123@gmail.com", Country = "India", Phone = 1234567890)            



QUESTION:-3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2,4,6,8,10,12,14,16,18,20].
An object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.
iter() methods is used to initialize the iterator object so that the instance of this object can be used for iterating.
list = [2,4,6,8,10,12,14,16,18,20]
myit = iter(list)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

Using For Loop.
for i in list: 
    myit = iter(list)
print(next(myit))    
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



QUESTION:-4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.
A Python generator function allows you to declare a function that behaves like an iterator, providing a faster and easier way to create iterators.
The yield keyword in python controls the flow of a generator function.
For example of a generator function:-
def test_fib1(): 
    a,b = 0,1
    while True: 
        yield a
        a,b = b , a+b
fib = test_fib1()
for i in range(10): 
    print(next(fib))        



QUESTION:-5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.
from math import sqrt
def is_prime(n): 
    if (n <= 1): 
        return False
    if (n == 2): 
        return True
    if (n % 2 == 0): 
        return False
    
    i = 3
    while i <= sqrt(n): 
        if n % i == 0: 
            return False
        i = i + 2
    return True

def prime_generator(): 
    n = 1
    while True: 
        n += 1
        if is_prime(n): 
            yield n

generator = prime_generator()
for i in range(150): 
    print(next(generator))

from itertools import islice
array = [x for x in islice(prime_generator(), 150)]                    



QUESTION:-6. Write a python program to print the first 10 fibonacci numbers using a while loop.
def test_fib1(): 
    a,b = 0,1
    while True: 
        yield a
        a,b = b , a+b
fib = test_fib1()
for i in range(10): 
    print(next(fib))        



QUESTION:-7. Write a List Comprehension to iterate through the given string:'pwskills'. Expected output:['p','w','s','k','i','l','l','s']   
h_letters = [ letter for letter in 'pwskills']
print(h_letters)



QUESTION:-8. Write a python program to check whether a given number is palindrome or not using a while loop.
num = int(input("Enter a value : "))
temp = num
rev = 0
while(num>0): 
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev): 
    print("This value is a palindrome number!") 
else: 
    print("This value is not a palindrome number!")       



QUESTION:-9. Write a code to print odd numbers from 1 to 100 using list comprehension.
Note:-Use a list comprehension to create a list from 1 to 100 and use another list comprehension to filter out odd numbers.
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
print(list(filter(lambda x : x%2 != 0 , l)))
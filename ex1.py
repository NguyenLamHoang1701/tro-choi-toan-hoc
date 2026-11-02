#ex1 
"""
a = int(input(" number 1 "))
b = int(input("number 2 "))
if a*b <= 1000:
    print(a*b)
else:
    print(a+b)
"""
#ex2 
"""
for i in range(10):
    j = i-1
    if i != 0:
        print("Current Number",i,"Previous Number",j, "Sum :", i+j )
    else:
        print("Current Number :0 Previous Number : 0 ,Sum : 0" )
"""
#ex3
"""
a = str(input("nwhjevy  :"))
for i in a:
    print(i)
"""
#ex4
"""
a = str(input("Enter a string: "))
b = int(input("num "))
a = a[b:]
print(a)
"""
#ex6
"""
a = int(input("Enter a number: "))
b = 1
for i in range(1,a+1):
    b = b*i
print(b)
"""
#ex7
"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.append("fig")
fruits.remove("banana")
print(fruits)
"""
#ex8
"""
text = "Python"
text = text[::-1]
print(text)
"""

# [::-1] is reverse in string 

#ex9
"""
sentence = "Learning Python is fun!"
a = 0
for i in sentence:
    if i == "a" or i=="e" or i =="i" or i =="o" or i=="u":
        a+=1
print(a)
"""
#ex10
"""
nums = [45, 2, 89, 12, 7]
print(max(nums), min(nums))
"""

#min(list) and max(list) is used to find the minimum and maximum value in a list


#ex11
"""
data = [1, 2, 2, 3, 4, 4, 4, 5]
seen = []
for i in data:
    if i not in seen:
        seen.append(i)
print(seen)
"""

#ex12
"""
nums = list(map(int,input().split()))

if nums[0] + nums[-1]:
    print("True")
else:
    print("False")

"""

#map() is func to applied every item 
#list() coverse map to list


#ex13
"""

a = list(map(int,input().split()))
b = []
for i in a:
    if i%5 ==0:
        b.append(i)
print(b)
"""

#ex14

"""
a = str(input("Enter a string: "))
b = 0
c = a.split() 
for i in c:
    if i == "Emma":
        b+=1
print(b)
"""
#or
"""
a = str(input("Enter a string: "))
b = a.count("Emma")
print(b)
"""
#c = a.split() is used to split string into list of words

#ex15 Worth rewatching
"""
a = int(input())
for i in range(1,a+1):
    for j in range(i):
        print(i,end = " ")
    print("\n")

"""
#\n is used to print new line



#ex16  Numerical Palindrome Check
"""
a = int(input("Enter a number: "))
b = str(a)
if b == b[::-1]:
    print("True")
else:
    print("False")
"""

#ex17  Merging Lists with Parity Filtering
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
seen = []
for i in list1:
    if i % 2 != 0:
        seen.append(i)
for j in list2:
    if j % 2 ==0:
        seen.append(j)
print(seen)

"""
#ex18 Integer Digit Extraction and Reversal

"""
a = int(input())
b = str(a)
c = b[::-1]
for i in c:
    print(i, end=" ")

"""
#ex19 Multi-Tiered Income Tax Calculation
"""
a = int(input("Enter your income: "))

if a <= 10000:
    tax = 0
    b = 0
elif a <= 20000:
    
    tax = (a - 10000) * 0.1 +b
    
else:
    b = 10000 * 0.1
    tax = (a - 20000) *0.2 + b
print(tax)

"""
#ex20 Nested Loops for Multiplication Tables
"""
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end = " ")
    print()

"""



#ex21   Downward Half-Pyramid Pattern
"""
a = int(input("Enter a number: "))
for i in range(a+1, 0, -1):
    for j in range(i):
        print("*", end= " ")
    print()
"""

#ex22 Custom Exponentiation Function

"""

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

def exponent(base, exp):
    a = 1
    for i in range(exp):
        a *= base
    return a
print(exponent(base,exp))
"""

#ex23 Check Palindrome Number
"""

a = int(input("Enter a number: "))
b = str(a)
if b == b[::-1]:
    print("True")
else:
    print("False")

"""

#ex24 Exercise 24. Generate Fibonacci Series
"""

a = int(input(" number: "))
fib = [0,1]
def fibonaci(n):
    for i in range(2,a):
        nums = fib[i-1]+ fib[i-2]
        fib.append(nums)
    return fib
print(fibonaci(a))

"""

#ex25 Check Leap Year
"""

a = int(input("...:"))
if a % 4 == 0 or a % 400 == 0:
    print(a," is leap year")
else:
    print(" not")


"""


#Exercise 26. Merging Two Dictionaries
"""

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
dict= dict1|dict2
print(dict)
"""

#or 
"""

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
dict1.update(dict2)
print(dict1)
"""


#Exercise 27. Finding Common Elements
"""

a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = list (set(a) & set(b))
print(c)
"""

# & la giao tuc la lay nhung cai trung nhau nma chio dung trong set
# | la hop tuc la cho ca 2 set thanh 1 va loaij bo cai trung
# - laf tru neus set1-set2 thi se chi lay set1 sau khi bo cac phan tu trung voi set2
#set dung de loc trung lap

#Exercise 28. Odd/Even List Splitter
"""

a = list(map(int,input().split()))
chan = []
le = []
for i in a:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)
print(chan)
print(le)
"""

#Exercise 29. Word Length Analysis
"""

a = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]


for i in a:
    print(i, len(i))
"""
# khong duoc quen len de de, so ki tu



#Exercise 30. Word Frequency Counter (The Histogram)
"""

text = str(input())
a = text.split()
b = {}

for i in a:
    if i in b:
        b[i]+= 1
    else:
        b[i] = 1
print(b)
"""

#Exercise 31. Print Alternate Prime Numbers
"""

a = int(input(" hfgey : "))
def prime_number(a):
    
    b = []
    
    for i in range(2, a+1): 
        c = 0
        for j in range(1,i+1):
            if i % j == 0:
                c += 1
            
        if c == 2:
            b.append(i)
    b = b[1::2]
    return b
print(prime_number(a))
"""


# [start:stop:step] nhu o teen thi di tu 0 va buoc la 2

#Exercise 32. Dictionary of Squares (Mapping Logic)
"""

a = int(input(" augfye :"))
b = {}
for i in range(1,a+1):
    b[i] = i**2
print(b)

"""
#Exercise 34. Print Reverse Number Pattern
"""

a = int(input(" hadg: "))
for i in range(a,0,-1):
    for j in range(i,0,-1): # voi moi i giam di thi luc in ra se giam so o dau 
        print(j, end = " ")
    print()
"""
#Exercise 35. Digit Detection in Strings
"""

a = str(input(" shfgy : "))
b = False
for i in a:
    if i.isdigit():
        b = True
print(b)
"""

# isdigit la ham de kiem tra do co phai la so khong


#Exercise 36. Capitalize First Letter (Title Case)
"""

text = " hello world form python language"
a = text.split()

b = " ".join(i.capitalize() for i in a)
print(b)
"""

#or
"""

text = " hello world form python language"
a = text.split()
d = []
for i in a:
    c = i.capitalize()
    d.append(c)
    b = " ".join(d)
print(b)
"""

#Exercise 37. Simple Countdown Timer
"""
a = int(input(" haef: "))
while a != 0:
    print(a, end= " ")
    a-= 1
else:
    print("Blast Off")
"""
#Exercise 38. File Creation and Basic I/O

"""
with open("note.txt","w") as file:
    file.write("hvehhrf wgfwu\n")
    file.write("h wgfwu\n")
    file.write("hvehhru\n")
# with open("name_file.txt", "w" for write   "r" for read) as file
with open("note.txt" , "r") as file:
    a = file.read()
    print(a)
"""
#Exercise 39. External File Word Counter
"""

with open("bf.txt","r") as file:
    a = file.read()
    print(a)
    b = a.split()
print(len(b))
"""
#Exercise 40. Introduction to Classes (OOP)

class car():
    def _init_(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print({self.name},{self.nodel},{self.make})
c = car("toyota","camry",2025)
c.start_engine()

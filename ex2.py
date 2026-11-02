#Exercise 1
"""

a = 1
while a<= 10:
    print(a)
    a+= 1
"""
#Exercise 2. Display numbers 
"""

for i in range(-10,0):
    print(i)
"""
#Exercise 3. Display a message
"""

for i in range(0,5):
    print(i)
    if i == 4:
        print("Done")
"""
#Exercise 4. Calculate the sum
"""

a = int(input(" gvfshdygcy: "))
b = 0
for i in range(a+1):
    b = b + i
print(b)
"""
#Exercise 5. Print multiplication table 

"""
a = int(input("havf: "))
for i in range(1,11):
    print(a*i)
"""
#Exercise 6. Calculate the cube
"""


a = int(input(" shbh: "))
for i in range(1,a+1):
    print(i**3)
"""

#Exercise 7. Display numbers
"""

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i % 5 ==0 and i<= 150:
        print(i)
    elif i > 500:
        break

"""
#Exercise 8. Count occurrences
"""


list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
a = 0
for i in list1:
    if target == i:
        a+= 1
print(a)
"""

#Exercise 9. Print elements
"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a = my_list[1::2]
print(a)"""
#Exercise 10. Print list
"""
list1 = [10, 20, 30, 40, 50]
print(list1[::-1])
"""
#or 
"""
list1 = [10, 20, 30, 40, 50]
print(list1.reverse())
"""
#Exercise 11. Reverse a string
"""
text = str(input())
a = ""
for i in text:
    a = i+a
print(a)
"""
# thay vi cong vao hom luon thi no se cong kieu nhuw la python -> ythonp vi them vao nen se ra sau

#Exercise 12. Count vowels and consonants vowels("aeiou")
"""


a =str(input("hgrf: "))
b = a.lower()
c = 0
d = 0
for i in b:
    if i == "a" or i == "e" or i == "i"  or i == "o" or i == "u":
        c+= 1
    elif i == " ":
        c = c
        d=d
    else:
        d+=1
print("vowel",c)
print("consonants",d)
"""
#or
"""
a = str(input(hvyw: ))
vowels = "aeiou"
b = 0
c = 0
for i in a.lower():
    if i in vowels:
        b+=1
    else:
        c+=1
print("vowels",b)
print("consonants",c)
"""
#Exercise 13. Count total number


"""
a = int(input("hyew: "))
c =0
while a !=0:
    a = a // 10
    c+=1
print(c)

"""
"""
#Exercise 14. Reverse an integer number
a = int(input("hvsf:"))
b = str(a)
print(b[::-1])
"""
#Exercise 15. Find largest and smallest digit
"""
a  =list(map(int,input("hgvefyh: ")))
print(max(a))
print(min(a))
"""
#Exercise 16. alindrome number
"""
a = int(input("bfy: "))
b = str(a)
if b == b[::-1]:
    print("yess")
else:
    print("no")
""" #string[start:end:step]

#Exercise 17. Find factorial of a number
"""
a = int(input("sjbv: "))
b = 1
for i in range(1,a+1):
    b = b*i
print(b)
"""
#Exercise 18. Collatz Conjecture






















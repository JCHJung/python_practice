# 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
from math import sqrt
from math import *
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')
print("\b")

# 2: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
n = int(input())
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)

# 3: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
new_dict = {}
n = int(input('please enter a number: '))
for i in range(1, n + 1):
    new_dict[i] = i * i
print(new_dict)

# 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98. Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
list4 = []
tuple4 = ()
for item in range(6):
    i = input('please enter a number: ')
    list4.append(i)

print(list4)
print(tuple(list4))

# 5: Define a class which has at least two methods: getString: to get a string from console input / printString: to print the string in upper case.


class manipulateString():
    def get_string(self):
        self.answ = input('enter your area: ')

    def print_string(self):
        print(self.answ.upper())


str1 = manipulateString()
str1.get_string()
str1.print_string()

# 6:
'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
'''
C, H = 50, 30


def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))


D = input().split(',')
D = list(map(calc, D))
print(",".join(D))

# 7: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.
x, y = map(int, input().split(','))
list_7 = []
for i in range(x):
    temp = []
    for j in range(y):
        temp.append(i*j)
    list_7.append(temp)

print(list_7)

# 8: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
list_8 = input().split(',')
list_8.sort()
print(list_8)

# 9: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.


def user_input():
    while True:
        answ_9 = input()
        if not answ_9:
            return
        yield answ_9


for line in map(str.upper, user_input()):
    print(line)

# 10: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
inp_string = input("Enter string: ").split()
out_string = []
for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))

# 11: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))

# 12: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
list_12 = []
for num in range(1000, 3001):
    if num % 2 == 0:
        list_12.append(num)

print(list_12)

lst = []
for i in range(1000, 3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j) % 2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))

# 13: Write a program that accepts a sentence and calculate the number of letters and digits.
word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
# two different types of formating method is shown in both solution
print(f"LETTERS {letter}\n{digits}")

# 14: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
string = input("Enter the sentense")
upper = 0
lower = 0
for x in string:
    if x.isupper() == True:
        upper += 1
    if x.islower() == True:
        lower += 1

print("UPPER CASE: ", upper)
print("LOWER CASE: ", lower)

# 15: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
a = input()
# N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)

# 16: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
list_16 = [str(int(item)**2) for item in input().split(',') if int(item) % 2]
print(",".join(list_16))

# 17: Write a program that computes the net amount of a bank account based a transaction log from console input.
total = 0
while True:
    s = input.split()
    if not s:
        break
    cm, num = map(str, s)

    if cm == 'D':
        total += int(num)
    if cm == 'W':
        total -= int(num)

print(total)

# 18:
'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
'''


def check(x):
    cnt = (6 <= len(x) and len(x) <= 12)
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == '@' or i == '#' or i == '$':
            cnt += 1
            break
    # counting if total 5 all conditions are fulfilled then returns True
    return cnt == 5


s = input().split(',')
# Filter function pick the words from s, those returns True by check() function
lst = filter(check, s)
print(",".join(lst))

# 19:
'''
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.
'''
lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

# here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(lst)

# 20: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


class generateNumber():
    def check(self, num):
        for i in range(0, int(num/7) + 1):
            yield i * 7


for i in generateNumber().check(int(input("please enter a number: "))):
    print(i)

# 21:
'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
'''
lst = []
position = [0, 0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))

# 22: Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically
ans = input().split()
word = sorted(set(ans))
for i in word:
    print("{0}:{1}".format(i, ans.count(i)))

# 23: Write a method which can calculate square value of number
n = int(input())
print(n ** 2)

# 24: Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# And add document for your own function
print(str.__doc__)
print(sorted.__doc__)


def pow(n, p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p


print(pow(3, 4))
print(pow.__doc__)

# 25: Define a class, which have a class parameter and have a same instance parameter.


class test():
    name = "default"

    def __init__(self, name=None):
        self.name = name


obj1 = test("player1")
print("%s name is %s" % (test.name, obj1.name))

# 26: Define a function which can compute the sum of two numbers.
num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))
print(f'the sum of {num1} and {num2} is {num1+num2}.')


# here lambda is use to define little function as sum
def sum(n1, n2): return n1 + n2


print(sum(1, 2))

# 27: Define a function that can convert a integer into a string and print it in console.
tstnum = int(input("please enter a number: "))
print(str(tstnum))


def conv(x): return str(x)


n = conv(10)
print(n)
print(type(n))

# 28: Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.


def check_number(num1, num2):
    print(sum(num1, num2))


def sum(s1, s2): return int(s1) + int(s2)


print(sum("10", "45"))

# 29: Define a function that can accept two strings as input and concatenate them and then print it in console.


def sum(s1, s2): return s1 + s2


print(sum("10", "45"))

# 30: Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.


def printLength(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len2 > len1:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
printLength(s1, s2)

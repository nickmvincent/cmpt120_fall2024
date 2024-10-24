# Author: Nick V
# Date: Oct 17, 2024
# Purpose: Show snippets from Week 1

print("Hello, World")
print("I have", 1)
# This is a comment
"""
Multi
line
string
"""

input()
variable = "example", # `=`, assignment
print(variable + " string"), # `" "` for strings and `+` for concat
mylist = [1,2,3] # `[ ]` for lists
import random # import
random.choice(my_list) # random.choice()
x = 5
y = 4
if x == y:  # example of condition
    print("if")
elif x == y+1:
    print("elif")
else:
    print("else")
5 > 3
5 >= 3
5 != 3
not 5 == 3
a = True
b = False
a and b
a or b
a and not b
(a and b) or (a or b)

my_string = "PYTHON."
my_string.lower()
my_string.upper()
my_string.strip(".")
"substring" in my_string # `in` (strings)
1 in [1,2,3] # `in` (lists)
for i in range(5):  # loop example
    print(i)

str(5)
int("5")

range(4)
range(1,5)
range(1,10,2)

x = 1
x += 1  # Accumulator pattern
print("Number: {:.3f}".format(myfloat))
print(
  type(17)`, `type(0.0)`, `type("xo")`, `type([1,2,3])`, `type(True)
)
print(
  2 ** 2, 3 * 4, 5 - 3, 4 + 4, 5 / 3, 5 // 3, 12 % 5
)
x=1
x = x + 1
x+=1
int(4.3)
float("123.45")
str(12.3)
len(my_list)
range(len(my_list))
print("Number: {:.3f}".format(myfloat))


file = open("myfile.txt")
line = file.readline()
for line in file:
  print(line)
lines = file.readlines()
my_list = my_string.split()
alist[2][0]  # Indexing in a list of lists
print(
  mystring[0], mystring[-1], mystring[:],
  mystring[3:5], mystring[:3], mystring[3:],
  mystring[3:-1]
)
"a"*3
["a"]*3
alist[2][0]
list1+list2
list1 = list1 + [elem]
"a" < "b"
"aa" < "ab"

list_a = [10, 30, 20, 30]
max_index = 0
max_val = list_a[0]
for i in range(len(list_a)):
  if list_a[i] > max_val:
    max_val = list_a[i]
    max_index = i
print(max_index, max_val)


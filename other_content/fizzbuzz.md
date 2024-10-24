# Fizzbuzz Variant

You must write a Python program to print every number between 1 and 30. Each number will be printed on a seperate line.

If a number is divisible by 3, also print " fizz" on the same line.

If a number is divisible by 5, also print " buzz" on the same line.

Example:
1
2
3 fizz
4
5 buzz


~~~

~~~

~~~

~~~

~~~

~~~

~~~

~~~

~~~

~~~

~~~

~~~



for i in range(1, 31):
    output = str(i)
    if i % 3 == 0:
        output += " fizz"
    if i % 5 == 0:
        output += " buzz"
    print(output)
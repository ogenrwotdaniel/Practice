## Practice from the book "Python Crash Course" by Eric Matthes


## Chapter 01 Getting Started
##It`s best to use lowercase letters and underscores for files and folders names because python uses these naming conventions for files and folders.


## BEST PROGRAMMING PRACTICES
## 1. when a program contains an error, the interpreter will display an error message that describes the problem that was encountered. (traceback is an error message that includes a record of what the program was doing when it encountered the error.)
## 2. Syntax errors occur when Python can`t interpret the code.
## 3. Step away from the computer and take a break if you can`t figure out what is wrong with your code.
## 4. The best way to learn a new programming language is to write code.
## 5. Start over again
## 6. Ask someone else for help
## 7. Use a search engine to search for the error message you are getting.
## 8. Use the Python documentation to look up the error message you are getting.
## 9. Ask for help online.

print("Hello World!")


## Chapter 02 Variables and Simple Data Types
##As you write your programs, your editor highlights different parts of your code in different colors. This color-coding is called syntax highlighting, and it makes your code easier to read.
##Variables are used to store values that can change throughout the life of a program. A variable is a label that you can use to refer to a value or set of values stored in memory.
## Rules for naming variables:
## 1. Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
## 2. Spaces are not allowed in variable names, so we use underscores to separate words in variable names.
## 3. Avoid using Python keywords and function names as variable names.
## 4. Variable names should be short but descriptive.
## 5. Be careful when using the lowercase letter l and the uppercase letter O because they can be confused with the numbers 1 and 0.
## 6. Python is case-sensitive, so the variable name message is different from Message.
## 7. Use the same case for all the letters in a variable name, or use underscores to separate words in a variable name.
## 8. Use descriptive variable names that convey the meaning of the values they store.


## 2.1 Assign a message to a variable and then print that message.
message = "Hello Python World!"
print(message)

## 2.2 Assign a new message to the variable and print that new message. Then change the value of the variable to a new message and print that new message.
message = "Hello Python Crash Course World!"
print(message)


## changing cases in strings
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


##using variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

## Adding whitespace to strings with tabs or newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

## Stripping whitespace
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

## Avoiding syntax errors with strings
message = "One of Python's strengths is its diverse community."
print(message)


##TRY IT YOURSELF
## 2-3. Personal Message: Store a person`s name in a variable, and print a message to that person. Your message should be simple, such as "Hello Eric, would you like to learn some Python today?"
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

## 2-4. Name Cases: Store a person`s name in a variable, and then print that person`s name in lowercase, uppercase, and titlecase.
name = "eric"
print(name.lower())
print(name.upper())


## 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f'{author} once said, "{quote}"')


## 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person`s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "{quote}"'
print(message)


## 2-7. Stripping Names: Store a person`s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so that the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = " \tAlbert Einstein\n "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

##2.8

## Numbers
## Integers are whole numbers, and floating-point numbers have decimal points.
## Python uses two multiplication symbols to represent exponents.
## Python supports the order of operations too, so you can use multiple operations in one expression.
## You can use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.
## Python will interpret any number with a decimal point as a floating-point number.
## If you mix an integer and a float in any other operation, you will get a float as the result.



##Flaots and Integers
print(3/2)
print(3.0/2)
print(3/2.0)

##Underscores in numbers
universe_age = 14_000_000_000
print(universe_age)

##Multiple assignments you cn assign multiple variables in one line. This can help shorten your programs and make them easier to read; you will use this technique often.
x, y, z = 0, 0, 0
print(x)
print(y)
print(z)


## Constants
## A constant is like a variable whose value stays the same throughout the life of a program. Python doesn`t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed.
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)


## TRY IT YOURSELF
## 2-9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)

## 2.801 Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this
print(5+3)
print(10-2)
print(4*2)
print(16/2)



## Chapter 03 Introducing Lists
## GENERAL INTRODUCTION
## A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don`t have to be related in any particular way.
## In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
## Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
## Index positions start at 0, not 1.
## To get the syntax for accessing an element from a list, you give the name of the list followed by the index of the item enclosed in square brackets.
## Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list.
## You can modify the elements in a list by referring to the index of the item you want to change.
## You can add elements to the end of a list using the append() method.
## You can add elements to a specific position in a list by using the insert() method.
## You can remove elements by their position in a list, or by the value of the item.
## The pop() method removes the last item in a list, but it lets you work with that item after removing it.
## If you know the position of the item you want to remove from a list, you can use the del statement.
## If you only know the value of the item you want to remove, you can use the remove() method.
## You can sort a list alphabetically, in either order, or in a specific order that you specify.
## You can reverse the original order of a list at any time by calling the reverse() method.
## The len() function returns the number of items in a list.
## Lists can hold millions of items, as long as your computer`s memory can hold the list.
## You can use individual values from a list just as you would any other variable.
## You can concatenate, or combine, lists using the addition operator (+).
## You can add new elements to a list by appending them.
## You can insert a new element at any position in your list by using the insert() method.
## You can remove an item according to its position in a list, or according to its value.
## If you know the position of the item you want to remove from a list, you can use the del statement.
## If you know the value of the item you want to remove, you can use the remove() method.
## You can sort a list permanently in alphabetical order using the sort() method.
## You can sort a list temporarily in alphabetical order using the sorted() function.

## accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])


##Index positions start at 0, not 1.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])




## Practice from the book "Python Crash Course" by Eric Matthes

from datetime import datetime

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


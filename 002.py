message = "Hello Python crush readers!"
print(message)

#Exercise page 19
#2.1 Assign a message to a variable, and then print that message

message = "This is my second last day in Daejeon"
print(message)
#2.2 2-2. Simple Messages: Assign a message to a variable, and print that message.
message = "A girl made me so so many crazy things I thought I would never do"
print(message)


##CHANGING CASE IN A STRING WITH METHODS
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())



##USING VARIABLES IN STRINGS
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

##ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")


##STRIPPING WHITESPACE
favorite_language = 'python '
print(favorite_language)


##Removing prefix and suffix whitespaces
simple_url = "https://www.example.com"
simple_url = simple_url.strip("https://")


## 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

## 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())


## 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f'{author} once said, "{quote}"')

## 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "{quote}"'
print(message)

## 2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = "\tAlbert Einstein\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

## 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)

## 2-9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)

## 2-10. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.
# This program prints a simple message.
message = "Hello Python world!"
print(message)

# This program prints a message about my favorite number.
favorite_number = 42
message = f"My favorite number is {favorite_number}."
print(message)

## 2-11. Zen of Python: Enter import this into a Python terminal session and skim through the additional principles.
import this

## 2-12. Favorite Number Remembered: Combine Exercise 2-9 and Exercise 2-10 into one file. If you remember, you can also include Exercise 2-11.
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)
import this

## 2-13. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.
# This program prints a simple message.
message = "Hello Python world!"
print(message
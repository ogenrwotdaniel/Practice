## Chapter 04 Working with Lists
## GENERAL INTRODUCTION

## Looping allows you to take the same action, or set of actions, with every item in a list. Python provides several ways to do this.
## You can use a for loop to work through each item in a list.
## You can use a for loop to work through a slice of a list.
## You can loop through a list using a for loop.
## You can create a numerical list using the range() function.
## You can use the range() function to tell Python to skip numbers in a given range.
## You can create a list of numbers using the range() function.
## You can perform simple statistics on a list of numbers.
## You can work with part of a list using slices.
## You can loop through a slice.
## You can copy a list by making a slice that includes the entire original list.
## You can copy a list by using a slice.
## You can use a for loop to generate a list of numbers.
## You can create a list of numbers using a for loop.
## You can create a list of numbers in one line using a list comprehension.
## You can work with part of a list using slices.

## Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

## A closer look at looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("{magician.title()}, that was a great trick!")
    print("I can`t wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

## Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("{magician.title()}, that was a great trick!")
    print("I can`t wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

## doing something after a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("{magician.title()}, that was a great trick!")
    print("I can`t wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

## Avoiding Indentation Errors
## Indentation errors occur when you don`t follow Python`s indentation guidelines.
## Indentation errors can be difficult to debug because spaces and tabs are invisible characters.

## Forgetting to Indent
## Always indent the line after the for statement in a loop.
## If you forget to indent the line after the for statement, Python will raise an indentation error.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

## Forgetting to Indent Additional Lines
## Always indent the additional lines of code that should run each time through the loop.
## If you forget to indent the additional lines of code, Python will raise an indentation error.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("{magician.title()}, that was a great trick!")
print("I can`t wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
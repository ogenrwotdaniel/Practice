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

##Using individual values from a list
##You can use individual values from a list just as you would any other variable.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a {bicycles[0].title()}."
print(message)

## 3.1 Names
names = ['John', 'James', 'Jenny', 'Jessica']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

## 3.2 Greetings
message = "Hello, {names[0]}!"
print(message)
message = "Hello, {names[1]}!"
print(message)
message = "Hello, {names[2]}!"
print(message)
message: str = "Hello, {names[3]}!"
print(message)

##3.3 Your Own List
cars = ['Audi', 'BMW', 'Mercedes', 'Toyota']
message = "I would like to own a {cars[0]} car."
print(message)
message = "I would like to own a {cars[1]} car."
print(message)
message = "I would like to own a {cars[2]} car."
print(message)
message = "I would like to own a {cars[3]} car."
print(message)

##Changing, Adding, and Removing Elements
## Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

## Adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

## Adding elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

## Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

## Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

## Removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

## Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

## Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

##3.4 Guest List
guests = ['John', 'James', 'Jenny', 'Jessica']
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")

##3.5 Changing Guest List
# noinspection PyRedeclaration
guests = ['John', 'James', 'Jenny', 'Jessica']
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")
print("{guests[0]} can`t make it to dinner.")
guests[0] = 'Jack'
print("Hello, {guests[0]}! You are invited to dinner.")

##3.6 More Guests (same as code line 406 - 421 but with additional guests)

##3.7 Shrinking Guest List
guests = ['John', 'James', 'Jenny', 'Jessica']
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")
print("I found a bigger dinner table.")
guests.insert(0, 'Jack')
guests.insert(2, 'Jill')
guests.append('Jerry')
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")
print("Hello, {guests[4]}! You are invited to dinner.")
print("Hello, {guests[5]}! You are invited to dinner.")
print("Hello, {guests[6]}! You are invited to dinner.")
print("I can only invite two people to dinner.")
print("Sorry, {guests.pop()}! I can`t invite you to dinner.")



## Organizing a List
## Sorting a list permanently with the sort() method
# noinspection PyRedeclaration
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

## Sorting a list permanently in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

## Sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

## Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

## Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

##3.8 Seeing the World
places = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

##3.9 Dinner Guests
guests = ['John', 'James', 'Jenny', 'Jessica']
print("I am inviting {len(guests)} guests to dinner.")

##3.10 Every Function
languages = ['Python', 'JavaScript', 'C', 'C++', 'Java']
print(languages)
print(sorted(languages))
print(languages)
print(sorted(languages, reverse=True))
print(languages)
languages.reverse()
print(languages)
languages.reverse()

##Avoiding Index Errors When Working with Lists
## Index errors occur when you try to access an index that doesn`t exist.
motorcycles = []
print(motorcycles[-1])

## TRY IT YOURSELF
## 3-11. Intentional Error: If you haven`t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

##3-12. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# noinspection PyRedeclaration
guests = ['John', 'James', 'Jenny', 'Jessica']
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")
print("I found a bigger dinner table.")
guests.insert(0, 'Jack')
guests.insert(2, 'Jill')
guests.append('Jerry')
print("Hello, {guests[0]}! You are invited to dinner.")
print("Hello, {guests[1]}! You are invited to dinner.")
print("Hello, {guests[2]}! You are invited to dinner.")
print("Hello, {guests[3]}! You are invited to dinner.")
print("Hello, {guests[4]}! You are invited to dinner.")
print("Hello, {guests[5]}! You are invited to dinner.")
print("Hello, {guests[6]}! You are invited to dinner.")

## Summary
## In this chapter you learned how to define a list and how to access and manipulate the elements in a list. You learned how to add elements to a list, remove elements from a list, and modify elements in a list.
##You learned how to sort a list, find the length of a list, and reverse the order of a list. You also learned how to avoid index errors when working with lists.

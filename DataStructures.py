import math

print("\n---\n\nPart 1: Lists\n")
#Part 1: Lists
#1. Create a list of 10 numbers.
list_1 = [13,25,32,48,51,36,27,84,69,10]
#2. Print the first, last, and middle number.
print(f"First: {list_1[0]}.\nLast: {list_1[-1]}.\nMiddle: {list_1[math.trunc(len(list_1)/2)]}.\n")
#3. Add a new number to the end of the list.
list_1.append(862)
#4. Replace the third number with 99.
list_1[2] = 99
#5. Loop through the list and print only the even numbers.
for item in list_1:
    if item % 2 == 0:
        print(str(item)+" is even.")

print("\n---\n\nPart 2: Dictionaries\n")
#Part 2: Dictionaries
#1. Create a dictionary of 5 countries and their capitals.
dict_1 = {"America": "Washington", "France": "Paris", "Japan": "Tokyo", "Germany": "Berlin", "Italy": "Rome"}
#2. Print the capital of 2 countries.
country_1 = "America"
country_2 = "Germany"
print(f"{dict_1[country_1]} is the capital of {country_1}.\n{dict_1[country_2]} is the capital of {country_2}.\n")
#3. Add a new country-capital pair.
dict_1["Ireland"] = "Dublin"
#4. Change the capital of one country.
dict_1["America"] = "New York"
#5. Loop through and print all countries and capitals.
for country_loop in dict_1:
    print(f"{country_loop}'s capital is {dict_1[country_loop]}")

print("\n---\n\nPart 3: Sets\n")
#Part 3: Sets
#1. Create a set of your favorite fruits.
set_fruits = {"Apple", "Banana", "Watermelon", "Strawberry", "Blueberry", "Plum", "Raspberry"}
#2. Add a new fruit, then remove one.
set_fruits.add("Peach")
set_fruits.remove("Raspberry")
#3. Create another set of fruits your friend likes.
set_friend_fruits = {"Apple", "Blackberry", "Dragonfruit", "Pear", "Watermelon", "Canteloupe", "Blueberry","Peach"}
#4. Print:
#   - Fruits you both like (intersection).
for shared_fruit in set_friend_fruits:
    if shared_fruit in set_fruits:
        print("Me and my friend both like "+shared_fruit)
print()
#   - Fruits only you like (difference).
for solo_fruit in set_fruits:
    if not(solo_fruit in set_friend_fruits):
        print("I like "+solo_fruit+", but my friend does not.")
print()
#   - All fruits either of you like (union).
set_all_fruits = set_fruits
set_all_fruits.update(set_friend_fruits)
for all_fruit in (set_all_fruits):
    print("Me or my friend like "+all_fruit)

print("\n---\n\nPart 4: Tuples\n")
#Part 4: Tuples
#1. Create a tuple of 5 colors.
color_tuple = ("Black", "Red", "Orange", "Blue", "White")
#2. Print the first and last color.
print("First color: "+color_tuple[0])
print("Last color: "+color_tuple[-1]+"\n")
#3. Loop through the tuple and print each color.
for color in color_tuple:
    print(color)
#4. Try to change one color (note the error).
try:
    color_tuple[0] = "Silver"
except TypeError:
    print("\nCannot assign items in Tuples.\n\n---\n")
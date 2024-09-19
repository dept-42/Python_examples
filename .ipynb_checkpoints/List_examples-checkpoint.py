# List examples
entry_number = 0

# 1. "declare a list and print it, simple print"
entry_number += 1
print(f"{entry_number}. declare a list and print it, simple print")
my_bikes = ["trek", "cannon", "schwin", "specialized"]
print(my_bikes)
print()
print("-" * 50)
print()

# 2 loop through list
entry_number += 1
print(f"{entry_number}. loop through list with 'for ... in ' ")
for bike in my_bikes:
    print(f"I own a {bike}")
print()
print("-" * 50)
print()

# 3. loop through list, print element with start-at-1 index number of each item
entry_number += 1
print(f"{entry_number}. loop through list, print element with start-at-1 index number of each item")
for bike in my_bikes:
    print(f"Bike  {my_bikes.index(bike)+1} in the list is a {bike}")
print()

# 4. Add an element to the end of a list with .append()
entry_number += 1
print(f"{entry_number}. Add an element to the end of a list with '.append()'")
my_bikes.append("raleigh")
print(my_bikes)
print()
print("-" * 50)
print()

# 5. Add an element to middle of a list
entry_number += 1
print(f"{entry_number}. Add an element to middle of a list")
my_bikes.insert(3, "marin")
print(my_bikes)
print()
print("-" * 50)
print()

# 6. Add an element to the begining fo a list (special case of insert)
entry_number += 1
print(f"{entry_number}. Add an element to the begining fo a list (special case of 'insert'")
my_bikes.insert(0, "peugeot")
print(my_bikes)
print()
print("-" * 50)
print()

# 7. remove an element from of a list with its index number
entry_number += 1
print(f"{entry_number}. remove an element from of a list with its index number")
print(f"7. before deleting index 3 {my_bikes}")
del my_bikes[3]
print(f"after deleting index 3 {my_bikes}")
print()
print("-" * 50)
print()

# 8. find the index and delete an item
entry_number += 1
print(f"{entry_number}. find the index and delete an item with 'del'")
my_bikes.insert(3, "schwin")
print(f"before deleting  {my_bikes}")
to_delete = "trek"
for bike in my_bikes:
    if bike == to_delete:
        print(f" to delete {my_bikes[my_bikes.index(bike)]} found!")
        this_index = my_bikes.index(bike)
        del my_bikes[this_index]
        print(f"after  deleting {to_delete} {my_bikes}")
        my_bikes.insert(this_index, bike)
        print(f"After reinserting {bike} {my_bikes}")
        break
print()
print("-" * 50)
print()

# 9.  Acomplish the same as 'find the index and delete' using .remove()
entry_number += 1
print(f"{entry_number}. Acomplish the same as 'find the index and delete' using '.remove()'")
to_delete = "marin"
my_bikes.remove(to_delete)
print(f"after  deleting {to_delete} {my_bikes} with '.remove()'")
# restore 'marin'
my_bikes.insert(4, to_delete)
print()
print("-" * 50)
print()

# 10. remove last list element with pop and capture removed value
entry_number += 1
print(f"{entry_number}. remove last list element with 'pop' and capture removed value:")
print(f"Before pop list is: {my_bikes}")
last_bike = my_bikes.pop()
print(f"popped element is: {last_bike}")
print(f"After pop list is: {my_bikes}")
my_bikes.append("raleigh")
print()
print("-" * 50)
print()

# 11.find the index and pop an item
entry_number += 1
print(f"{entry_number}. find the index and pop an item")
print(my_bikes)
print(f"before pop  {my_bikes}")
to_pop = "trek"
for bike in my_bikes:
    if bike == to_pop:
        print(f" to pop {my_bikes[my_bikes.index(bike)]}")
        this_index = my_bikes.index(bike)
        this_bike = my_bikes.pop(this_index)
        print(f"after  popping {to_pop} {my_bikes}")
        my_bikes.insert(this_index, this_bike)
        print(f"After reinserting {bike}: {my_bikes}")
        break
print()
print("-" * 50)
print()

# 12. delete a list inside a list using .remove()
entry_number += 1
print(f"{entry_number}. delete a list inside a list using .remove() '.remove()'")
my_bikes.insert(3,["mountain", "bmx"])
to_delete = ["mountain", "bmx"]
print(f"before  deleting {to_delete} {my_bikes} with '.remove()'")
my_bikes.remove(to_delete)
print(f"after  deleting {to_delete}: {my_bikes} with '.remove()'")
print()
print("-" * 50)
print()

# 13 sort a list alphabetically with list.sort(); NOTE case matters.
entry_number += 1
print(f"{entry_number}. sort a list alphabetically with list.sort(); NOTE case matters.")
same_case_letters = ["c","b", "a"]
mixed_case_letters = ["c","B","a"]

print(f"unsorted same_case_letters: {same_case_letters}")
same_case_letters.sort()
print(f"sorted same_case_letters: {same_case_letters}")
print()
print(f"unsorted mixed_case_letters: {mixed_case_letters}")
mixed_case_letters.sort()
print(f"sorted mixed_case_letters: {mixed_case_letters}")
print()
print("-" * 50)
print()


# 14 sort a list of number as strings with list.sort(), numerically
entry_number += 1
print(f"{entry_number}. sort a list of number as strings with list.sort(), numerically")
numbers_as_strings = ["1", "3", "10", "5"]
print(f"numbers_as_strings {numbers_as_strings}")
numbers_as_strings.sort()
print(f"numbers_as_strings sorted as strings: {numbers_as_strings}")
print("now sort the list as integers")
numbers_as_strings_numerically_sorted = [int(x) for x in numbers_as_strings]
numbers_as_strings_numerically_sorted.sort()
print(f"numbers_as_strings_numerically_sorted: {numbers_as_strings_numerically_sorted}")
print()
print("-" * 50)
print()

# 15. sort a list with 'sorted(list), leaving original list unchaged
entry_number += 1
print(f"{entry_number}. sort a list with 'sorted(list), leaving original list unchaged")
same_case_letters = ["c","b", "a"]
print(f"unsorted same_case_letters: {same_case_letters}")
print(f"temporarily sorted same_case_letters: {sorted(same_case_letters)}")
print(f"original same_case_letters: {same_case_letters}")
print()
print("-" * 50)
print()

# 16. reverse a list with 'list.reverse'. NOTE: this is NOT reverse alphabetivcal sorting
entry_number += 1
print(f"{entry_number}. reverse a list with 'reverse(list)'. NOTE: this is NOT reverse alphabetivcal sorting")
print(f"original my_bikes: {my_bikes}")
my_bikes.reverse()
print(f"reversed my_bikes: {my_bikes}")
my_bikes.reverse()
print(f"restored original order with second call to 'reverse': {my_bikes}")
print()
print("-" * 50)
print()

# 17. use 'sorted()' and  'list.reverse' to print in temporrary reverse alphabetical order
entry_number += 1
print(f"{entry_number}. use 'sorted()' and  'list.reverse' to print in temporrary reverse alphabetical order")
print(f"original my_bikes: {my_bikes}")
revBikes = sorted(my_bikes)
print(f"reversed alphabetical my_bikes: { revBikes}")
print(f"original order unchaged: {my_bikes}")
# NOTE sorted(my_bikes).reverse() DOES NOT WORK
print()
print("-" * 50)
print()

# 18. use 'len(list)' to find the lengh ( = number of imtems in ) a list
entry_number += 1
print(f"{entry_number}. use 'len(list)' to find the lengh ( = number of imtems in ) a list")
print(f"my_bikes: {my_bikes}")
length_my_bikes = len(my_bikes)
print(f"length of  my_bikes: {length_my_bikes}")
print()
print("-" * 50)
print()

# 19. use 'rang(x, y, [z])' to make a list of numbers
entry_number += 1
print(f"{entry_number}.use 'rang(x, y, [z])' to make a list of numbers")
number_list_1 = list()
number_list_1 = range(1, 6)
print(f"number_list_1: {number_list_1}")
print()
print(f"{entry_number}.use 'range(x, y, z)' to make a list of numbers, in steps of 'z' ")
print(" eg: number_list_2 = list(range(2, 21,2)) makes a list of even number up to 20 ")
number_list_2 = list(range(2, 21,2))
print(f"number_list_2: {number_list_2}")
length_my_bikes = len(my_bikes)
print(f"length of  my_bikes: {length_my_bikes}")
print()
print(f"{entry_number}.use 'rang(x, y, [z])' and a for loop to make a list of squares")
squares = list()
for value in range(1,11):
    squares.append(value ** 2)
print(f"squares: {squares}") 
print()
print("-" * 50)
print()

# 20. use 'min', 'max' ans 'sum' to find the largerst,  smallest and sum of list 
entry_number += 1
print(f"{entry_number}.use 'min', 'max' ans 'sum' to find the largerst,  smallest and sum of list ")
number_list = range(1,10)
print(f"number_list: {number_list}") 
print(f"the smallest number:  {min(number_list)}")
print(f"the largestest number:  {max(number_list)}")
print(f"sum of all the list numbers:  {sum(number_list)}")
print()
print("-" * 50)
print()

# 21. some binary fun
entry_number += 1
print(f"{entry_number}.some binary fun ")
number_list = range(1,10)
binary =list()
for i in range(0,10,2):
    binary.append( 2 ** i)
    print(f"{i} {binary} {sum(binary)}")
print()
binary =list()
for i in range(1,10,2):
    binary.append( 2 ** i)
    print(f"{i} {binary} {sum(binary)}")
print()
print("-" * 50)
print()


#22. use list comprehension to calculate all cubesw from 1 to 10
entry_number += 1
print(f"{entry_number}.use list comprehension to calculate all cubesw from 1 to 10 ")
cubes = [number ** 3 for number in range(1, 11)]
print(f"cubes from 1 to 10:  {cubes}")
print()
print("-" * 50)
print()
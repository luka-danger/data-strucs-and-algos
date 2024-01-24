# Hash Table is dictionary in Python 
# Hash Set is just a set

# Create an empty dictionary (Hash Table)
emptyHashTable = {}

# Dictionary (Hash Table) 
# Unordered and no duplicate keys
# Can only hash keys 
data = {'Caleb': 'email@mail.com', 'Bob': 'bob@email.com', 'Susan': 'hi@email.org'}

# If you are planning on changing data for objects: 
# Can make data non-hashable by using __hash__
class Test:
    __hash__ = None 

# Set 
colors = {"green"}
# Create an empty set 
fruits = set()

first_colors = {'red', 'blue', 'green', 'purple', 'magenta'}
second_colors = {'yellow', 'magenta', 'orange', 'pink', 'green'}

# Difference
only_first_colors = first_colors - second_colors
print(only_first_colors)

# Union - no repetition 
all_colors = first_colors | second_colors
print(first_colors.union(second_colors))
print(all_colors)

# Intersection - repeats allowed
intersecting_colors = first_colors & second_colors
print(first_colors.intersection(second_colors))
print(intersecting_colors)


import pandas as pd

# Hash table OR Hashmap is a type of data structure that maps
# keys to its value pairs

# it's literally the dictionary in python

print("Creating a dictionary")

my_dict = {'Dave': '001', 'Ana': '002', 'Joe': '003'}
print(my_dict, type(my_dict))

print("Other way to create:")

new_dict = dict(Dave='001', Ana='002')
print(new_dict)

print("=" * 30)
print("Nested dictionaries are basically dictionaries that lie in other dictionaries")

emp_details = dict(Employee=dict(Dave=dict(ID='001', Salary=2000, Designation='Team-lead'),
                                 Ana=dict(ID='002', Salary=1000, Designation='Associate')))
print(emp_details)

print("=" * 30)
print("Accessing items")

print("Value of key Dave:", my_dict['Dave'])  # The value of an element
print("Value of key Dave:", my_dict.get('Dave'))  # Another way to get the value of an element

print("All values in the dictionary", my_dict.values())  # All values in the dictionary

# Access via loop repetition
print("The keys of the dictionary")

for x in my_dict:
    print(x)

print("=" * 12)

# Access all the terms of the dictionary

for x, y in my_dict.items():
    print(x, y)     # x, y -> key, value

print("=" * 30)
print("Updating items")

my_dict['Dave'] = '004'
my_dict['Chris'] = '003'  # Adding a new term
print(my_dict)

print("=" * 30)
print("Deleting. There are many ways to delete a term in dictionary")

print(my_dict.pop('Ana'))  # Delete 'Ana' and return the value (002)

print(my_dict.popitem())  # Remove the last element and return a (key, value) pair as a 2-tuple.

del my_dict['Dave']  # Just remove Dave, don't return nothing
print(my_dict)

print("=" * 30)

print("Converting Dictionary into a pandas Dataframe (matrix)")

df = pd.DataFrame(emp_details['Employee'])
print(df)


# Better for loops
inventory_names = ["Screws", "Wheels", "Metal parts", "rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421,23, 43]

for name, number in list(zip(inventory_names, inventory_numbers)):
    print(name, number)

# List comprehension
one_to_one_hundred = [num for num in range(0,100)]
print(one_to_one_hundred)

one_to_ten_then_zero = [num if num < 10 else 0 for num in range(0,100)]
print(one_to_ten_then_zero)

# combine list comprehsion
combin_comp = [[x for x in range(5)]for y in range(10)]
for row in combin_comp:
    print(row)

# Other comprehensions
set_comp = {num for num in range(100)}
print(set_comp)
dict_comp = {num: num for num in range(100)}
print(dict_comp)
tuple_comp = tuple(num for num in range(100)) 
print(tuple_comp)

# Sorting Data
list1 = [4,1,3,5,2]
print(sorted(list1))

list2 = [('a',3), ('b',10), ('c',6),('d',5)]
def sort_function(item) -> int:
    return item[1]    
print(sorted(list2, key=sort_function))
print(sorted(list2, key=lambda item: item[1]))
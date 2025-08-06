my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)  # Output: [10, 20, 30, 40]
my_list.insert(1, 15)  # Insert 15 at index 1
print(my_list)  # Output: [10, 15, 20, 30, 40]
my_list.extend([50, 60,70])  # Extend list with multiple elements
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]
my_list.remove(70)  # Remove the first occurrence of 20
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
my_list.sort()  # Sort the list in ascending order
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
#find and print th index of 30
index_of_30 = my_list.index(30)
print(index_of_30)  # Output: 3
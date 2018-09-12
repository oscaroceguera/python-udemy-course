my_variable = 'hello'
grades = [77, 80, 90]
tuple_grades = (77, 80, 90 ) # immutable
set_grades = {77, 80, 90} # unique & unordered

# print(sum(grades) / len(grades))
# print(set_grades)

# grades.append(100)
# print(grades)

# tuple_grades = tuple_grades + (100,)
# print(tuple_grades)

# print(grades[0])

grades[0] = 60
# print(grades)

# tuple_grades[0] = 60
# print(tuple_grades) # error immutable

# set_grades[0] = 60
# print(set_grades) # no support item assigment# 

set_grades.add(60)
set_grades.add(60)
# print(set_grades)

## Set operations

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

# print(your_lottery_numbers.intersection(winning_numbers))
# print(your_lottery_numbers.union(winning_numbers))
# print({1,2,3,5}).difference({1,2})

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))
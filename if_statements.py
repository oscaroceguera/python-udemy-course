# should_continue = True
# if should_continue:
#   print('heelo')

# know_people = ['John', 'Ana', 'Mary']
# person = input('Enter the person you know:')

# if person in know_people:
#   print('you know {}!'.format(person))
# else:
#   print('You dont know {}!'.format(person))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Modify the method below to make sure only even numbers are returned.
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number % 2 == 0:
#           evens.append(number)
#     return evens

# print(even_numbers())

## Exercise

def who_do_you_know():
  people = input('Enter the names of people you know, separate by commas: ')
  people_list = people.split(',') # ['John', 'Ana', 'Mary']

  # OPTION ONE
  # people_without_spaces = []
  # for person in people_list:
  #   people_without_spaces.append(person.strip())

  # OPTION TWO
  people_without_spaces = [person.strip() for person in people_list]

  return people_without_spaces

def ask_user():
  person = input('Enter a name of some you Know ')
  if person in who_do_you_know():
    print('You know {}!'.format(person))
  else:
    print('You dont know {}!'.format(person))

ask_user()
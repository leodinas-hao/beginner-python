'''
if test_expression:
  # NOTE: THE INDENTATION
  # statement(s) to be run
else:
  # statement(s) to be run


if test_expression:
  # statement(s) to be run
elif test_expression:
  # statement(s) to be run
elif test_expression:
  # statement(s) to be run
else:
  # statement(s) to be run
'''

# Example 1:  if ... else...
# a = 27
# b = 93
# if a >= b:
#   print(f'{a} is greater than or equal to {b}')
# else:
#   print(f'{b} is greater than {a}')


# Example 2: if ... elif ...
# a = 27
# b = 27
# if a < b:
#   print(f'{a} is less than {b}')
# elif a == b:
#   print(f'{a} is equal to {b}')


# Example 3:  if ... elif ... else ...
# a = 27
# b = 93
# if a < b:
#   print(f'{a} is less than {b}')
# elif a > b:
#   print(f'{a} is greater than {b}')
# else:  # a == b
#   print(f'{a} is equal to {b}')


# Example 4: nested if statements
a = 16
b = 25
c = 27
if a > b:
  if b > c:
    print(f'{a} is greater than {b} and {b} is greater than {c}')
  else:
    print(f'{a} is greater than {b} and less than {c}')
elif a == b:
  print(f'{a} is equal to {b}')
else:
  print(f'{a} is less than {b}')

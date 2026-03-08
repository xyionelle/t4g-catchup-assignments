# Task One
first_name: str = 'Thelma'
last_name: str = 'Pharin'
age: int = 27
programming_concept: str = 'variables'
print(first_name, last_name, age, programming_concept)


# Task Two
print(first_name + ' ' + last_name)
print(f'{first_name} {last_name}')
full_name: str = f'{first_name} {last_name}'


# Task Three
print(full_name.lower())
print(full_name.upper())
print(full_name.lower().count('a'))
space_index = full_name.index(' ')
full_name = 'Coder' + full_name[space_index:]


# Task Four
print(
    f'Hi, I am {full_name}. '
    f'I am {age} years old and my favourite concept '
    f'so far is {programming_concept}.'
)


# Task Five
first_charcter = full_name[0]
print(first_charcter)
last_character = full_name[-1]
print(last_character)
first_name_only = full_name[:full_name.index(' ')]
print(first_name_only)
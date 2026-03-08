name: str = 'thelma pharin'
cohort: str = 'Tech 4 Girls'
age: int = 27
favorite_topic: str = 'variables'
current_week: int = 4

# string methods
name = name.title()
favorite_topic = favorite_topic.replace('variables', 'data types')

# calculation
weeks_left = 12 - current_week

# profile card output
print('======== PROFILE CARD ========')
print(f'Name: {name}')
print(f'Cohort: {cohort.upper()}')
print(f'Age: {age}')
print(f'Favourite Topic: {favorite_topic}')
print(f'Current Week: {current_week}')
print('------------------------------')
print(f'Weeks left in program: {weeks_left}')
print('==============================')
from datetime import date
person = {}
person['first_name'] = input('Enter first name: ')
person['second_name'] = input('Enter second name: ')
person['third_name'] = input('Enter third name: ')
person['birth_year'] = int(input('Enter birth year: '))
person['current_age'] = date.today().year - person['birth_year']
print(person)

from random import randint

n = int(input('Enter sides: '))
first_roll = randint(1, n);
second_roll = randint(1, n);
third_roll = randint(1, n);

print ('First roll: ' + str(first_roll))
print ('Second roll: ' + str(second_roll))
print ('Third roll: ' + str(third_roll))
print('Sum is: ' + str(first_roll + second_roll + third_roll))

from random import randint

n = int(input('Enter dice side: '))
player1 = input('Enter player1 name: ')
player2 = input('Enter player2 name: ')

player1_score = randint(1, n)
print('{0} rolls: {1}'.format(player1, str(player1_score)))
player2_score = randint(1, n)
print('{0} rolls: {1}'.format(player2, str(player2_score)))

if player1_score > player2_score:
	print(player1 + ' wins!')
elif player1_score < player2_score:
	print(player2 + ' wins!')
else: 
	print('Equal!')

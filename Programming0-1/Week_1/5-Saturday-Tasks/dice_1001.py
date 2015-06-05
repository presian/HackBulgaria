from random import randint as rand 

player1_name = input('Please enter first player name: ')
player2_name = input('Please enter second player name: ')

player1_score = 1001
player2_score = 1001

def dice_roll(player_name):
	daces = rand(1, 30)
	print('***Player: {0}***\nroll: {1}'.format(player_name, daces)) 
	return daces

while True:
	player1_score += dice_roll(player1_name) * (-1 if (player1_score > 0) else 1)
	print('score: {0}'.format(player1_score))
	player2_score -= dice_roll(player2_name) * (-1 if (player1_score > 0) else 1)
	print('score: {0}\n======================'.format(player2_score))
	if player1_score == 0 or player2_score == 0:
		print('{0} wins!'.format(player1_name 
			if (player1_score == 0) 
			else player2_name))
		break

import random
player_wins=0
computer_wins=0
while player_wins<3:
	print("make your guess:", end=" ")
	guess = str(input())
	guess = guess.lower()
	choices = ['rock', 'paper' , 'scissors']
	computer_guess = random.choice(choices)
	print('you guessed' , guess)
	print('computer guessed', computer_guess)
	if guess in choices:
		if guess == computer_guess:
			print("its a tie!")
		elif guess == 'rock':
			if computer_guess == 'scissors':
				print("you win!")
				player_wins= player_wins+1
			elif computer_guess == 'paper':
				print("you lose!")
				computer_wins+=1
		elif guess == 'paper':
			if computer_guess =='rock':
				print("you win!")
				player_wins+=1
			elif computer_guess == 'scissors':
				print("you lose!")
				computer_wins+=1
		elif guess == 'scissors':
			if computer_guess == 'paper':
				print("you win!")
				player_wins+=1
			if computer_guess == 'rock':
				print("you lose!")
				computer_wins+=1
	print("you've won ", player_wins)





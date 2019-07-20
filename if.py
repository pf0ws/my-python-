number='23'
guess = input('enter an integer : ')
if guess == number:
	print('That\'s right')
elif guess>number:
	print('a little bigger')
else:
	print('a little lower')
print('done')
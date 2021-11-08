import random

res = random.randint(1, 99)
end = 0
print ("This is an interactive guessing game!")
print ("You have to enter a number between 1 and 99 to find out the secret number.")
print ("Type 'exit' to end the game.")
print ("Good luck!")
count = 0
while end == 0:
	print ("\nWhat's your guess between 1 and 99?")
	stdin = input (">> ")
	if stdin == "exit":
		print ("LOOSER")
		end = 1
	else:
		if stdin.isdecimal() == False:
			print ("That's not a number.")
		else:
			nb = int (stdin)
			if nb == res:
				if res == 42:
					print ("The answer to the ultimate question of life, the universe and everything is 42.")
				if count == 0:
					print("Congratulations, you've got it on your first try!")
				else:
					print("Congratulations, you've got it in " + str(count) + " attempt !")
				end = 1
			elif nb < res:
				print ("Too low!")
			else:
				print ("Too high!")
			count += 1
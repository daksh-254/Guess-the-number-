#importing
import random
import math

# Taking Inputs
start = 1
end = 10

print("Guess a number between", start, "and", end)

# generating random number
x = random.randint(start, end)

#chances
print("\nYou have 4 chances to guess the correct number!\n")

# Start no of guesses
count = 0

# for calculation of number of guesses
while count < math.log(end - start + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count," attempts!")
		break
	elif x > guess:
		print("Try a higher number")
	elif x < guess:
		print("Try lower number")

# Ran out of guesses
if count >= math.log(end - start + 1, 2):
	print("\nThe number is %d" % x)
	print("You just ran out of chances!\n")

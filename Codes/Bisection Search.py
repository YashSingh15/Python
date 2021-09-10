# Program to find cube root of a number using an approximation algorithm

cube = float(input("Enter a number whose cube root you want to find: "))

guess = 0.0
increment = 0.0001
epsilon = 0.001
num_guesses = 0

high = abs(cube)
low = 0

if abs(cube) < 1:
    high = 1

guess = (high + low)/2  # choose guess to be midway between the two extremes

while abs(guess ** 3 - abs(cube)) >= epsilon:

    if guess ** 3 < abs(cube):
        low = guess     # If guess < cube, all values lower than guess must also be < cube. So we make guess our new lower bound

    else:
        high = guess    # If guess > cube, all values higher than guess must also be > cube. So we make guess our new upper bound

    guess = (high + low)/2

    num_guesses += 1

if cube < 0:
        guess = -guess

print(f"Cube root of {cube} is close to {round(guess, 2)}")
print(f"It took us {num_guesses} guesses to get to the solution!")

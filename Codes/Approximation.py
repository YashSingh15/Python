# Program to find cube root of a number using an approximation algorithm

cube = float(input("Enter a number whose cube root you want to find: "))

guess = 0.0
increment = 0.0001
epsilon = 0.001
num_guesses = 0


while abs(guess ** 3 - abs(cube)) >= epsilon and guess <= abs(cube):
    guess += increment
    num_guesses += 1

if abs(guess ** 3 - abs(cube)) >= epsilon:
    print("Cannot find the cube root of this number using this method")
else:
    if cube < 0:
        guess = - guess

    print(f"Cube root of {cube} is close to {round(guess, 2)}")
    print(f"It took us {num_guesses} guesses to get to the solution!")

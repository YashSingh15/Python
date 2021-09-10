# Program to find cube root of a number using a guess and check (exhaustive enumeration) algorithm

cube = int(input("Enter a number whose cube root you want to find: "))

for guess in range(abs(cube) + 1):
    if guess ** 3 >= cube:
        break

if guess ** 3 != abs(cube):
    print(f"{cube} is not a perfect cube")
else:
    if cube < 0:
        guess = -guess

    print(f"The cube root of {cube} is {guess}")

print("Hello world!")
num = int(input("Input your number:")) #initiating program with number
def find_factors():
    factors = []
    for i in range(1, num + 1): #finding the factors of a given number
        if num % i == 0:
            factors.append(i) #adding the factors to a list
    for j in factors: #Loop with if-else statements
        if j % 2 == 0:
            print(f"{j} is even number.")#checking if the factor is even
        else:
            print(f"{j} is odd number.")#checking if the factor is odd
    return factors

find_factors()

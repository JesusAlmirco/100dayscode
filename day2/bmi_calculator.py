height = input('Enter your height in M: ')
weigth = input('Enter your weigth in Kg: ')
# Using the exponent operator **
# bmi = int(weigth) / float(height) ** 2
# Or using Multiplication and PEMDAS
bmi = int(weigth) / (float(height) * float(height))
result = int(bmi)
print(result)

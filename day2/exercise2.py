"""Create a program using maths and f-Strings that tells us
how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message
with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers. """

age = input('What is your current age?: ')

final_age = 90 - int(age)

days = int(final_age) * 365
weeks = int(final_age) * 52
years = int(final_age) * 12

message = f"You have {days} days, {weeks} weeks, and {years} months left."
print(message)

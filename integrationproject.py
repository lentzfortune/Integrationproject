# Lentz Fortune
# Waffle House Kiosk
import random


def age():
    year_today = (int(input("Enter the year: ")))
    day_today = int(input("Enter the day: "))
    month = int(input("Enter the month "))

    year2 = (int(input("Enter your birth year: ")))
    birthday = (int(input("Enter the day of your birth: ")))
    birth_month = int(input("Enter the month of your birth "))

    age = year_today - year2

    if age < 16:
        print("You must be atleast 16 years old to apply.")

    # agereached = ((birth_month - 1) * 30) + birthday
    # print (agereached)
    # daysinyear = ((month - 1) * 30) + day_today
    # print(daysinyear)

    # if agereached > daysinyear:
    #   age = age - 1


allstar = 15.75
hashbrowns = 3.5
eggs = 3.5
bacon = 3.75
waffle = 5
topping = 0.5
total = 0
print("Welcome to Waffle House!")
name = input("Who is this All Star for? Please enter your name: ")

order_eggs = (input("Would you like eggs (Y/N): "))
if (order_eggs == ("Y")) or (order_eggs == str("y")):
    total = total + eggs
elif (order_eggs == ("N")) or (order_eggs == str("n")):
    allstar = allstar - eggs
else:
    allstar = allstar - eggs

order_bacon = (input("Would you like bacon (Y/N): "))
if (order_bacon == ("Y")) or (order_bacon == ("y")):
    total = total + bacon
elif (order_eggs == ("N")) or (order_bacon == ("n")):
    allstar = allstar - bacon
else:
    allstar = allstar - bacon

order_hashbrowns = str(input("Would you like hashbrowns (Y/N): "))
if (order_hashbrowns == str("Y")) or (order_hashbrowns == str("y")):
    total = total + hashbrowns
elif (order_eggs == str("N")) or (order_bacon == str("n")):
    allstar = allstar - hashbrowns
else:
    allstar = allstar - hashbrowns

order_bacon = str(input("Would you like a waffle (Y/N): "))
if (order_bacon == str("Y")) or (order_bacon == "y"):
    total = total + waffle
elif (order_eggs == str("N")) or (order_bacon == "n"):
    allstar = allstar - waffle
else:
    allstar = allstar - waffle

veteran_discount = str(input("Are you a veteran (Y/N): "))
if (veteran_discount == str("N")) or (veteran_discount == str("n")):
    print("We'll give you the discount anyway: ")

discounted = total * 0.25
discounted_price = total - discounted

print("Your total is $", format(discounted_price, '.2f'), sep="")

# examples

# exponents: ** two stars are used to raise numbers to a power
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
exponents = num1 ** num2
print(exponents)
# division: does division,  can outputs decimals
division = num1 / num2
print(division)
# floor division: outputs whole numbers, it rounds down
floor_division = num1 // num2
print(floor_division)
# modulus: modulus gives the remainder.
# It is helpful in determining whether a number is dividable by another number
modulus = num1 % num2
print(modulus)

interested = input("Are you interested in employment at a Waffle House: (Y/N) ")
if (interested == ("Y")) or (interested == ("y")):
    total = total + bacon
elif (interested == ("N")) or (interested == ("n")):
    print("Thank you for coming " + name, end='')
    print(" you are awsome!")
    quit()

lastName = input("Enter your last name: ")
firstName = input("Enter your first name: ")


age()

applicationID = random.randint(1, 101)

workExperience = int(input("How many employers have you had: "))
count = 0
for i in range(workExperience):
    count += 1
    employer = input("What was the name of the employer: ")
    role = input("What was your role: ")

educational_institutions = int(input("How many educational Institutions have you attended: "))
count2 = 0
while count2 != educational_institutions:
    count2 += 1
    institution = input("What was the name of the institution: ")
    skill = input("What skill did you acquire: ")


print("Thank you for your application. Keep in touch.")

#how to use and boolean
num3 = int(input("Please enter the number 2: "))
num4 = int(input("Please enter the number 3: "))
if (num3 == 2) and (num4 == 3):
    print("Goodjob!")

num5 = 3
num6 = 7
# using not boolean
print(not num5 > num6)







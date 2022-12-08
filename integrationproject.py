"""The goal of this program is to provide waffle house with a kiosk for their Allstar, their most popular menu item. """
__author__ = "Lentz Fortune"


def main():
    sprint_one_and_two()
    waffle_house_kiosk()
    employment_opportunity = input("Are you interested in employment at Waffle House? ")
    if employment_opportunity == "y" or employment_opportunity == "Y":
        application()


def sprint_one_and_two():
    """The purpose of this function is to show proficiency in using python operators by asking the user to input
     a few numbers  """
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
    # how to use and boolean
    num3 = int(input("Please enter the number 2: "))
    num4 = int(input("Please enter the number 3: "))
    if (num3 == 2) and (num4 == 3):
        print("Goodjob!")

    num5 = 3
    num6 = 7
    # using not boolean
    print(not num5 > num6)


def add_to_order(total, item, item_price):
    """The purpose of this function is to ensure that the user enters only enter a y or u. The parameters item and
    item_price get assigned outside the function."""
    good_answer = False
    while not good_answer:
        answer = input("Would you like to add " + str(item) + " Y/N ")
        if answer == "Y" or answer == "y":
            total = total + item_price
            good_answer = True
        else:
            if answer != "N" or answer != "n":
                print("please enter a Y or an N")
            else:
                good_answer = True
    return total


def waffle_house_kiosk():
    """The kiosk function it ask the user if they want an item and adds the price to the total. """
    total = 0
    print("Welcome to Waffle House!")
    name = input("Who is this All Star for? Please enter your name: ")

    item = "eggs"
    item_price = 3.5
    total = add_to_order(total, item, item_price)

    item = "bacon"
    item_price = 3.75
    total = add_to_order(total, item, item_price)

    item = "waffle"
    item_price = 5
    total = add_to_order(total, item, item_price)

    item = "hash browns"
    item_price = 3.5
    total = add_to_order(total, item, item_price)

    discounted = total * 0.25

    veteran = input("Are you a veteran Y/N: ")
    if veteran == "Y" or veteran == "y":
        total = total - discounted

    print("Your total is: ", "%.2f" % total)


def application():
    """If the user is interested in employment at waffle house, they can fill out an application at the kiosk. The
    function ask the use to enter their age, educational level, and work experience."""
    ok_input = False
    while not ok_input:
        try:
            birth_year = int(input("Please enter the year of your birth: "))
            ok_input = True
        except ValueError:
            print("Please enter a whole number or a number greater than 1920")

    days_alive = 2022 - birth_year
    if days_alive < 16:
        print("Must be at least 16 to apply.")
        exit()
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")

    valid_input = False
    while not valid_input:
        try:
            work_experience = int(input("How many employers have you had: "))
            valid_input = True
        except ValueError:
            print("Please enter a whole number.")

    count = 0
    for i in range(work_experience):
        count += 1
        employer = input("What was the name of the employer: ")
        role = input("What was your role: ")
    good_input = False
    while not good_input:
        try:
            educational_institutions = int(input("How many educational Institutions have you attended: "))
            good_input = True
        except ValueError:
            print("Please enter a whole number.")
    count2 = 0
    while count2 != educational_institutions:
        count2 += 1
        institution = input("What was the name of the institution: ")
        skill = input("What skill did you acquire: ")

    print("Thank you,", first_name, "for your application. Keep in touch.")


main()

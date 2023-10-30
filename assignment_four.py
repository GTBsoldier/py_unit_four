# Lars Leonard - Cook
# 10-27-2023
# This code calculates an adventure park ticket based off of age and county.

def get_cost(age, county): # function that calculates the cost of the ticket based on the age and county entered
    base_price = 70 # base price of ticket with no discounts applied
    if age < 0:
        return -1
    if age < 5:
        return 0.0
    elif age >= 65:
        if county == "pg":
            return base_price * 0.4625
        elif county == "m":
            return 30.0
        else:
            return base_price*.5
    if county == "m":
        return 60.0
    if county == "h" and age < 14:
        return base_price - (base_price * .18)
    else:
        return base_price
def main(): # main function that when called, runs the program as intended
    print("Hello, welcome to the Adventure Park at Sandy Spring Friends School!")

    age = int(input("How old are you?: ")) # prompts user for an age, must be a value of zero or above
    county = input("What county do you live in?(Choose m for Montgomery county, h for Howard county, "  
                   "and pg for Prince Georges county: ") # prompts user for county of residence, allowing
                                                         # for only three options
    final_cost = get_cost(age, county) # final cost of the ticket that the individual will pay

    if age < 0: # if statement that sends an error message if a value below zero is entered,
                # along with a guide for the right kind of number to send
        print("Invalid age, please enter a positive number.")
    else:
        print("The ticket will cost", final_cost, "dollars.")

main() #runs the main function
#This project will calulate and display travel expenses, by adding up all the cost and subtracting it from the user's budget.
#4/5/2023
#CTI-110 P1HW2 - Travel Expense
#Jon Graves
#

#These prompts will ask the user to input basic information about their travel plans.
print("This program calculates and displays travel expenses")
user_budget = int(input('Enter Budget: '))
user_destination = input('Enter you travel destination: ')
user_gas = int(input('How much do you think you will spend on gas? '))
user_hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))
user_food = int(input('Last, how much do you need for food? '))
print()

print('------------Travel Expenses------------')

#These prompts will output all the information the user has inputed.
print('Location:', user_destination)
print('Initial Budget:', user_budget)
print()
print('Fuel:', user_gas)
print('Accomodation:', user_hotel)
print('Food:', user_food)
print()

#This line will add up the expenses and subtract it from the user's budget to show the user's remains.
user_balance = user_budget - (user_gas + user_hotel + user_food)

print('Remaining Balance:', user_balance) 

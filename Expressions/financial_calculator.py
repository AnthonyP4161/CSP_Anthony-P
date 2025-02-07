# Anthony Petersen, Financial Calculator

#welcome user and explains programs use
print("Welcome, this is a financial calculator to calculate your expenses, savings, and spendings")
#have user input monthly income
income = float(input("What is your income in number amount: "))
#have user input cost of rent
rent = float(input("How much does your rent cost: "))
#have user input cost of utilities
utilities = float(input("How much does your utilities such as power, water, etc. cost: "))
#have user input cost of groceries
groceries = float(input("How much do your groceries cost on average monthly: "))
#have user input cost of transportation
transportation = float(input("How much does transportation cost monthly: "))
#calculate how much they put into savings (10% of income)(income*.1)
savings = income*.1
#calculate how much is spending(income minus savings and expenses)
spending_money = float(income - savings - rent - utilities - groceries - transportation)
#calculate percent of income used for rent (rent/income *100)
percent_rent = float(rent/income *100)
#calculate percent of income used for utilities (utilities/income *100)
percent_utilities = float(utilities/income *100)
#calculate percent of income used for groceries (groceries/income *100)
percent_groceries = float(groceries/income *100)
#calculate percent of income used for transportation (transportation/income *100)
percent_transportation = float(transportation/income *100)
#calculate percent of income used for savings (savings/income *100)
percent_savings = float(savings/income *100)
#calculate percent of income used for spending (spending/income *100)
percent_spending = float(spending_money/income *100)
#print the following

    #your rent is $ which is % of your income
print("Your rent is", rent, "which is",percent_rent,"% of your income")
    #your utilities is $ which is % of your income
print("Your utilties is", utilities, "which is",percent_utilities,"% of your income")
    #your groceries is $ which is % of your income
print("Your groceries is", groceries, "which is",percent_groceries,"% of your income")
    #your transportation is $ which is % of your income
print("Your transportation is", transportation, "which is",percent_transportation,"% of your income")
    #your savings is $ which is % of your income
print("Your savings is", savings, "which is",percent_savings,"% of your income")
    #your spending is $ which is % of your income
print("Your spending money leftover is", spending_money, "which is",percent_spending,"% of your income")
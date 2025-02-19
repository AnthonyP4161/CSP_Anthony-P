# Anthony Petersen, Financial Calculator

print("Welcome, this is a financial calculator to calculate your expenses, savings, and spendings")
def inputs():
    income = float(input("What is your income in number amount: "))
    rent = float(input("How much does your rent cost: "))
    utilities = float(input("How much does your utilities such as power, water, etc. cost: "))
    roceries = float(input("How much do your groceries cost on average monthly: "))
    transportation = float(input("How much does transportation cost monthly: "))
    savings = income*.1
def percents():
    spending_money = float(income - savings - rent - utilities - groceries - transportation)
    percent_rent = float(rent/income *100)
    percent_utilities = float(utilities/income *100)
    percent_groceries = float(groceries/income *100)
    percent_transportation = float(transportation/income *100)
    percent_savings = float(savings/income *100)
    percent_spending = float(spending_money/income *100)
inputs()
percents()
print("Your rent is", rent, "which is",percent_rent,"% of your income")

print("Your utilties is", utilities, "which is",percent_utilities,"% of your income")

print("Your groceries is $", groceries, "which is",percent_groceries,"% of your income")

print("Your transportation is $", transportation, "which is",percent_transportation,"% of your income")

print("Your savings is $", savings, "which is",percent_savings,"% of your income")

print("Your spending money leftover is", spending_money, "which is",percent_spending,"% of your income")
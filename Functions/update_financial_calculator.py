# Anthony Petersen, Update Financial Calculator

print("Welcome, this is a financial calculator to calculate your expenses, savings, and spendings")
def inputs(type):
    return input(f"What is your {type} in a number amount: \n")
income = float(inputs("income"))
rent = float(inputs("rent"))
utilities = float(inputs("utilities"))
groceries = float(inputs("groceries"))
transportation = float(inputs("transportation"))
savings = income *.1
spending = income - rent - utilities - groceries - transportation - savings

def percentages(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent:.2f}% of your income")

percentages(rent, income, "rent")
percentages(utilities, income, "utilties")
percentages(groceries, income, "groceries")
percentages(transportation, income, "transportation")
percentages(savings, income, "savings")
percentages(spending, income, "spending")
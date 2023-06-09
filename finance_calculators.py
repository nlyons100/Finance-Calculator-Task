import math
investment_definition = "investment - to calculate the amount of interest you'll earn on your investment" 
bond_definition = "bond - to calculate the amount you'll have to pay on a home loan"
# Displays the definition of the term investment used in this program
print(investment_definition) 
# Displays the definition of the term bond used in this program 
print(bond_definition) 
# Asks the user to select investment or bond 
program_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# If user enters inorrect selection, prints an error message and asks them to make a correct selection
if len(program_selection) < 4 : 
    print("You have entered an invalid selection. Please enter 'investment' or 'bond'")
elif len(program_selection) > 10 : 
    print(("You have entered an invalid selection. Please enter 'investment' or 'bond'"))
# Calculates the investment amount based on user input for defined variables below and selection of simple or compound interest 
if program_selection == "investment" : 
    deposit = int(input(("Enter the amount of money you are depositing: ")))
    interest_rate = int(input ("Enter the interest rate, as a percentage, but only enter the number of the percentage: "))
    investment_years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter your selection of simple or compound interest: ")
    if interest_type == "simple" : 
        total_investment_simple = int(deposit*(1 + ((interest_rate/100) * investment_years)))
        print(total_investment_simple)
    if interest_type == "compound" : 
        total_investment_compound = int(deposit * math.pow((1+(interest_rate/100)), investment_years))
        print(total_investment_compound)
# Calculates how much the user will have to repay each month based on their input for the defined variables below
if program_selection == "bond" : 
   property_value = int(input(("Enter the present value of your house: ")))
   interest_rate_bond = int(input ("Enter the interest rate: "))
   repayment_time= int(input("Enter the number of months you plan on repaying the bond: "))
   repayment = int((((interest_rate_bond/100)/12) * property_value) / (1 - (1 + interest_rate_bond)**(-repayment_time)))
   print("You will repay the following amount of money each month: " + str(repayment))










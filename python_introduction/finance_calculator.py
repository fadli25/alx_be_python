# Prompt the user for financial details
try:
    monthly_income = float(input("Enter your monthly income: "))
    total_monthly_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - total_monthly_expenses
    
    # Project annual savings with a 5% interest rate
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * 0.05)
    
    # Output the results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
    
except ValueError:
    print("Please enter valid numeric values for income and expenses.")

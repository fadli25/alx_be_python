# Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings using an intermediate variable
savings_before_interest = monthly_income - total_monthly_expenses

# Calculate the annual savings and projected savings including interest
total_annual_savings = savings_before_interest * 12
interest = total_annual_savings * 0.05
projected_savings = total_annual_savings + interest

# Output the results
print(f"Your monthly savings are ${savings_before_interest:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

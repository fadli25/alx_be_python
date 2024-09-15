def main():
  """
  Calculates monthly savings and projected annual savings with interest.
  """
  # User Input
  income = float(input("Enter your monthly income: "))
  expenses = float(input("Enter your total monthly expenses: "))

  # Calculate Monthly Savings
  monthly_savings = income - expenses

  # Project Annual Savings (Simplified Formula)
  annual_interest_rate = 0.05  # 5% annual interest rate
  projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

  # Output Results
  print(f"Your monthly savings are ${monthly_savings:.2f}.")
  print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
  main()
def calculate_savings(income, expenses):
  """
  Calculates monthly savings and projected annual savings with interest.

  Args:
    income: Monthly income.
    expenses: Monthly expenses.

  Returns:
    A tuple containing monthly savings and projected annual savings.
  """

  if income <= expenses:
    raise ValueError("Monthly income must be greater than or equal to monthly expenses.")

  monthly_savings = income - expenses
  annual_interest_rate = 0.05  # 5% annual interest rate
  projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)
  return monthly_savings, projected_savings

def main():
  """Main entry point for the program."""

  try:
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))

    monthly_savings, projected_savings = calculate_savings(income, expenses)

    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
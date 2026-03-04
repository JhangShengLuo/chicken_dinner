from langchain_core.tools import tool

@tool
def calculate_affordability(item_cost: float, down_payment: float, monthly_income: float, monthly_expenses: float, loan_term_months: int, annual_interest_rate: float) -> str:
    """
    Calculates if a user can afford a specific item based on their income, expenses, and loan terms.
    """
    loan_amount = item_cost - down_payment
    if loan_amount <= 0:
        return "You can pay for this entirely with your down payment. No loan needed."

    monthly_interest_rate = (annual_interest_rate / 100) / 12
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / loan_term_months
    else:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**loan_term_months) / ((1 + monthly_interest_rate)**loan_term_months - 1)

    disposable_income = monthly_income - monthly_expenses
    affordability_ratio = monthly_payment / monthly_income

    status = "Highly Affordable"
    if affordability_ratio > 0.36:
        status = "High Risk - Monthly payment exceeds 36% of gross income"
    elif monthly_payment > disposable_income:
        status = "Unaffordable - Monthly payment exceeds disposable income"

    return f"Estimated Monthly Payment: ${monthly_payment:.2f}\nDisposable Income Before Loan: ${disposable_income:.2f}\nAffordability Status: {status}"

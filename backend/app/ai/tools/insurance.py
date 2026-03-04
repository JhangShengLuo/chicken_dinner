from langchain_core.tools import tool

@tool
def compare_life_insurance(age: int, coverage_amount: float, term_years: int = 20) -> str:
    """
    Compares Term Life Insurance vs Whole Life Insurance estimates.
    """
    base_rate_term = 1.5 if age < 30 else (2.5 if age < 50 else 5.0)
    base_rate_whole = 10.0 if age < 30 else (18.0 if age < 50 else 35.0)

    est_term_monthly = (coverage_amount / 100000) * base_rate_term * (term_years / 20)
    est_whole_monthly = (coverage_amount / 100000) * base_rate_whole

    return f"1. Term Life ({term_years} years): ~${est_term_monthly:.2f}/mo (No cash value)\n2. Whole Life: ~${est_whole_monthly:.2f}/mo (Builds cash value)"

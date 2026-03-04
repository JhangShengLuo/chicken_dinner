from langchain_core.tools import tool
from typing import Optional

@tool
def extract_life_stage(age: Optional[int] = None, marital_status: Optional[str] = None, dependents: Optional[int] = None, annual_income: Optional[float] = None) -> str:
    """
    Call this tool when the user mentions their age, marital status, dependents, or income.
    """
    updated_fields = []
    if age is not None: updated_fields.append(f"Age: {age}")
    if marital_status is not None: updated_fields.append(f"Marital Status: {marital_status}")
    if dependents is not None: updated_fields.append(f"Dependents: {dependents}")
    if annual_income is not None: updated_fields.append(f"Annual Income: ${annual_income}")

    if not updated_fields:
        return "No life stage information provided."

    return f"Successfully extracted: {', '.join(updated_fields)}."

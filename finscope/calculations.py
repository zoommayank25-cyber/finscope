"""Transparent, dependency-light financial calculations."""

def _non_negative(name: str, value: float) -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative.")


def simple_interest(principal: float, annual_rate_percent: float, years: float) -> float:
    """Return simple interest: principal × rate × time."""
    _non_negative("principal", principal)
    _non_negative("annual_rate_percent", annual_rate_percent)
    _non_negative("years", years)
    return principal * (annual_rate_percent / 100) * years


def compound_interest(
    principal: float, annual_rate_percent: float, years: float, compounds_per_year: int = 1
) -> float:
    """Return future value with a fixed nominal annual rate and periodic compounding."""
    _non_negative("principal", principal)
    _non_negative("annual_rate_percent", annual_rate_percent)
    _non_negative("years", years)
    if compounds_per_year <= 0:
        raise ValueError("compounds_per_year must be greater than zero.")
    if principal == 0:
        return 0.0
    return principal * (1 + (annual_rate_percent / 100) / compounds_per_year) ** (
        compounds_per_year * years
    )


def investment_return(initial_value: float, final_value: float):
    """Return total holding-period return in percent, or None if initial value is zero."""
    _non_negative("initial_value", initial_value)
    _non_negative("final_value", final_value)
    if initial_value == 0:
        return None
    return ((final_value - initial_value) / initial_value) * 100


def inflation_adjusted_value(amount: float, annual_inflation_percent: float, years: float) -> float:
    """Estimate future cost of today's basket using a constant annual inflation rate."""
    _non_negative("amount", amount)
    _non_negative("annual_inflation_percent", annual_inflation_percent)
    _non_negative("years", years)
    return amount * (1 + annual_inflation_percent / 100) ** years

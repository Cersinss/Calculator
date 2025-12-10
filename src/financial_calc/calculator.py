def _validate_non_negative(*values: float) -> None:
    if any(value < 0 for value in values):
        raise ValueError("Аргументы должны быть неотрицательными")


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    _validate_non_negative(principal, rate, time)
    return principal * rate * time / 100


def calculate_compound_interest(
    principal: float, rate: float, time: float, n: int = 1
) -> float:
    _validate_non_negative(principal, rate, time)
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    return principal * (1 + rate / (100 * n)) ** (n * time)


def calculate_tax(amount: float, tax_rate: float) -> float:
    _validate_non_negative(amount, tax_rate)
    if not 0 <= tax_rate <= 100:
        raise ValueError("Ставка налога должна быть между 0 и 100")
    return amount * tax_rate / 100


import math

import pytest

from financial_calc.calculator import (
    calculate_compound_interest,
    calculate_simple_interest,
    calculate_tax,
)


class TestCalculateSimpleInterest:
    def test_calculates_interest_examples(self) -> None:
        assert calculate_simple_interest(1000, 5, 2) == 100.0
        assert calculate_simple_interest(1500, 3.5, 4) == 210.0

    def test_zero_values(self) -> None:
        assert calculate_simple_interest(0, 5, 3) == 0
        assert calculate_simple_interest(1000, 0, 1) == 0
        assert calculate_simple_interest(1000, 5, 0) == 0

    def test_negative_values_raise(self) -> None:
        with pytest.raises(ValueError):
            calculate_simple_interest(-1000, 5, 2)
        with pytest.raises(ValueError):
            calculate_simple_interest(1000, -5, 2)
        with pytest.raises(ValueError):
            calculate_simple_interest(1000, 5, -2)


class TestCalculateCompoundInterest:
    def test_calculates_interest_examples(self) -> None:
        assert calculate_compound_interest(1000, 5, 2) == pytest.approx(1102.5)
        assert calculate_compound_interest(2000, 7, 3, n=4) == pytest.approx(
            2462.8786, rel=1e-4
        )

    def test_zero_values(self) -> None:
        assert calculate_compound_interest(0, 5, 2) == 0
        assert calculate_compound_interest(1000, 0, 2) == 1000
        assert calculate_compound_interest(1000, 5, 0) == 1000

    def test_invalid_arguments_raise(self) -> None:
        with pytest.raises(ValueError):
            calculate_compound_interest(-1000, 5, 2)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, -5, 2)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, -2)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, 2, n=0)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, 2, n=-1)
        with pytest.raises(ValueError):
            calculate_compound_interest(1000, 5, 2, n=1.5)  # type: ignore[arg-type]


class TestCalculateTax:
    def test_calculates_tax_examples(self) -> None:
        assert calculate_tax(1000, 13) == 130
        assert calculate_tax(2500, 20) == 500

    def test_zero_values(self) -> None:
        assert calculate_tax(0, 13) == 0
        assert calculate_tax(1000, 0) == 0

    def test_invalid_arguments_raise(self) -> None:
        with pytest.raises(ValueError):
            calculate_tax(-1000, 13)
        with pytest.raises(ValueError):
            calculate_tax(1000, -1)
        with pytest.raises(ValueError):
            calculate_tax(1000, 120)


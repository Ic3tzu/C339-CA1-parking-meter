import pytest
from src.parking_fee import calculate_parking_fee

# CA1 test file
# Spec 3.1, requirements 1 and 2:
# 200 cents for every started hour, and 0 minutes costs 0.
@pytest.mark.parametrize(
    ("minutes", "expected_fee"),
    [
        (0, 0),  # zero minutes costs zero
        (1, 200),  # lower boundary of the first hour
        (59, 200),  # just under one hour
        (60, 200),  # upper boundary of the first hour
        (61, 400),  # just into the second hour
        (120, 400),  # upper boundary of the second hour
        (121, 600),  # just into the third hour
        (600, 2000),  # exactly 10 hours
        (601, 2200),  # one minute into the 11th hour
    ],
)
def test_valid_minutes_charges_200_cents_per_started_hour(minutes, expected_fee):
    # Act and Assert
    result = calculate_parking_fee(minutes)
    assert result == expected_fee


# Spec 3.1 output: the fee must be an integer number of cents.
@pytest.mark.parametrize("minutes", [0, 60, 90])
def test_valid_minutes_returns_int(minutes):
    # Act
    result = calculate_parking_fee(minutes)
    # Assert
    assert type(result) is int


# Spec 2, requirement 4: correct type but outside the range -> ValueError.
@pytest.mark.parametrize("minutes", [-1, -60, -1000])
def test_negative_minutes_raises_value_error(minutes):
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_parking_fee(minutes)


# Spec 2, requirements 2 and 3: bool is not a valid int, wrong type -> TypeError.
@pytest.mark.parametrize("minutes", ["60", 60.0, 59.5, None, True, False, [60]])
def test_non_int_minutes_raises_type_error(minutes):
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_parking_fee(minutes)

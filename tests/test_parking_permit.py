import pytest
from src.parking_permit import is_permit_valid


# Spec 3.2, requirement 1: valid only when the permit is active
# and the stay is at most 120 minutes (zero included).
@pytest.mark.parametrize(
    "parked_minutes",
    [
        0,  # zero minutes is included
        1,
        60,
        119,
        120,  # upper boundary, still valid
    ],
)
def test_active_permit_within_120_minutes_returns_true(parked_minutes):
    # Act
    result = is_permit_valid(True, parked_minutes)
    # Assert: "is True" so that 1 is not accepted as True (spec 3.2 output)
    assert result is True


# Spec 3.2, requirement 2: an inactive permit or a stay above 120 is not valid.
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (True, 121),  # just above the boundary
        (True, 1000),  # far above the boundary
        (False, 0),  # inactive permit, shortest stay
        (False, 60),
        (False, 120),  # inactive permit, at the boundary
        (False, 121),  # inactive and too long
    ],
)
def test_inactive_permit_or_over_120_minutes_returns_false(permit_active, parked_minutes):
    # Act
    result = is_permit_valid(permit_active, parked_minutes)
    # Assert: "is False" so that 0 is not accepted as False (spec 3.2 output)
    assert result is False


# Spec 2, requirement 4: correct type but outside the range -> ValueError.
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (True, -1),
        (False, -1),
        (True, -120),
    ],
)
def test_negative_parked_minutes_raises_value_error(permit_active, parked_minutes):
    # Act and Assert
    with pytest.raises(ValueError):
        is_permit_valid(permit_active, parked_minutes)


# Spec 2, requirements 2 and 3: permit_active accepts only True or False.
@pytest.mark.parametrize("permit_active", [1, 0, "True", "yes", None])
def test_non_bool_permit_active_raises_type_error(permit_active):
    # Act and Assert
    with pytest.raises(TypeError):
        is_permit_valid(permit_active, 60)


# Spec 2, requirements 2 and 3: bool is not a valid int, wrong type -> TypeError.
@pytest.mark.parametrize("parked_minutes", ["60", 60.0, 59.5, None, True, False])
def test_non_int_parked_minutes_raises_type_error(parked_minutes):
    # Act and Assert
    with pytest.raises(TypeError):
        is_permit_valid(True, parked_minutes)

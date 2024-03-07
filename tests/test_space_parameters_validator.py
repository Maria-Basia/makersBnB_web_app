import pytest

from lib.space_parameters_validator import SpaceParametersValidator

def test_is_valid():
    validator = SpaceParametersValidator("Space_4", "Description_4", "345", "2024-03-10", "2024-03-15")
    assert validator._is_valid() == True

def test_is_not_valid_with_bad_name():
    validator_1 = SpaceParametersValidator("", "Description_5", "345.5", "2024-03-10", "2024-03-15")
    assert validator_1._is_valid() == False
    validator_2 = SpaceParametersValidator(None, "Description_6", "56.5", "2024-03-10", "2024-03-15")
    assert validator_2._is_valid() == False

def test_is_not_valid_with_bad_description():
    validator_1 = SpaceParametersValidator("Space_8", "", "345.5", "2024-03-10", "2024-03-15")
    assert validator_1._is_valid() == False
    validator_2 = SpaceParametersValidator("Space_9", None, "56.5", "2024-03-10", "2024-03-15")
    assert validator_2._is_valid() == False

def test_is_not_valid_with_bad_price():
    validator_1 = SpaceParametersValidator("Space_8", "Description_8", "", "2024-03-10", "2024-03-15")
    assert validator_1._is_valid() == False
    validator_2 = SpaceParametersValidator("Space_9", "Description_9", None, "2024-03-10", "2024-03-15")
    assert validator_2._is_valid() == False



def test_generate_errors():
    validator_1 = SpaceParametersValidator("", "", "", "", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Description must not be blank",
        "Price must be a number"
    ]
    validator_2 = SpaceParametersValidator("", "Description_9", "56.5", "2024-03-10", "2024-03-15")
    assert validator_2.generate_errors() == [
        "Name must not be blank"
    ]

    validator_3 = SpaceParametersValidator("Space_8", "", "456", "2024-03-10", "2024-03-15")
    assert validator_3.generate_errors() == [
        "Description must not be blank"
    ]

    validator_4 = SpaceParametersValidator("Space_8", "Description_8", "", "2024-03-10", "2024-03-15")
    assert validator_4.generate_errors() == [
        "Price must be a number"
    ]

def test_get_valid_name_if_name_valid():
    validator_1 = SpaceParametersValidator("space_1", "Description_1", "789", "2024-03-10", "2024-03-15")
    assert validator_1.get_valid_name() == "space_1"

def test_get_valid_name_refuses_if_invalid():
    validator_1 = SpaceParametersValidator("", "Description_1", "567", "2024-03-10", "2024-03-15")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Cannot get valid name"


def test_get_valid_description_if_description_valid():
    validator_1 = SpaceParametersValidator("Title", "Description", "87", "2024-03-10", "2024-03-15")
    assert validator_1.get_valid_description() == "Description"

def test_get_valid_description_refuses_if_invalid():
    validator_1 = SpaceParametersValidator("Title","", "654", "2024-03-10", "2024-03-15")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_description()
    assert str(err.value) == "Cannot get valid description"


def test_get_valid_price_if_price_valid():
    validator_1 = SpaceParametersValidator("Title", "Description", "87", "2024-03-10", "2024-03-15")
    assert validator_1.get_valid_price() == "87"

def test_get_valid_price_refuses_if_invalid():
    validator_1 = SpaceParametersValidator("Title","Description", "", "2024-03-10", "2024-03-15")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_price()
    assert str(err.value) == "Cannot get valid price"
import pytest
from unittest.mock import patch
from src.main import main

@patch('builtins.input', side_effect=['1', '+', '2', 'no'])
@patch('builtins.print')
def test_valid_addition(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Result: 3.0")

@patch('builtins.input', side_effect=['1', 'x', '2', '1', '+', '1', 'no'])
@patch('builtins.print')
def test_invalid_operator(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Invalid operator.")

@patch('builtins.input', side_effect=['a', '1', '+', '1', 'no'])
@patch('builtins.print')
def test_non_numeric_input_first_number(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Invalid input. Please enter numbers only.")

@patch('builtins.input', side_effect=['1', '+', 'b', '1', '+', '1', 'no'])
@patch('builtins.print')
def test_non_numeric_input_second_number(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Invalid input. Please enter numbers only.")

@patch('builtins.input', side_effect=['1', '/', '0', '1', '+', '1', 'no'])
@patch('builtins.print')
def test_division_by_zero_main(mock_print, mock_input):
    main()
    mock_print.assert_any_call("An error occurred: float division by zero")
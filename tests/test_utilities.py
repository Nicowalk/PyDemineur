import pytest
from utilities import (
    is_there_a_mine,
    is_already_revealed,
    reveal_neighbor_0_cases,
    is_end_of_game,
    check_board_dimensions,
)

def test_is_there_a_mine():
    list_of_mines = [(0, 2), (2, 2)]
    assert is_there_a_mine(0, 2, list_of_mines) == True
    assert is_there_a_mine(1, 1, list_of_mines) == False

def test_is_already_revealed():
    list_of_cases_revealed = [(0, 0), (1, 1)]
    assert is_already_revealed(0, 0, list_of_cases_revealed) == True
    assert is_already_revealed(2, 2, list_of_cases_revealed) == False

def test_reveal_neighbor_0_cases():
    board = [
        [0, 0, -1],
        [1, 2, 1],
        [0, 1, -1]
    ]
    cases_revealed = []
    reveal_neighbor_0_cases(0, 0, board, cases_revealed)
    assert (0, 0) in cases_revealed
    assert not (1, 0) in cases_revealed
    assert (0, 1) in cases_revealed

    # Test edge cases
    cases_revealed = []
    reveal_neighbor_0_cases(-1, 0, board, cases_revealed)
    assert cases_revealed == []

    cases_revealed = []
    reveal_neighbor_0_cases(0, -1, board, cases_revealed)
    assert cases_revealed == []

    cases_revealed = []
    reveal_neighbor_0_cases(3, 0, board, cases_revealed)
    assert cases_revealed == []

    cases_revealed = []
    reveal_neighbor_0_cases(0, 3, board, cases_revealed)
    assert cases_revealed == []

def test_is_end_of_game():
    assert is_end_of_game(3, 3, 2, 7) == True
    assert is_end_of_game(3, 3, 2, 6) == False

def test_check_board_dimensions():
    assert check_board_dimensions(3, 3) == True
    assert check_board_dimensions(0, 3) == False
    assert check_board_dimensions(3, 0) == False
    assert check_board_dimensions(3, 101) == False
    assert check_board_dimensions(101, 3) == False
    assert check_board_dimensions(3, 3, max_size_board=2) == False
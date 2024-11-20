import pytest
import sys

sys.path.insert(1, "./src")
from utilities import (
    is_there_a_mine,
    is_already_revealed,
    reveal_neighbor_0_cases,
    is_end_of_game,
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
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    cases_revealed = []
    reveal_neighbor_0_cases(0, 0, 3, 3, board, cases_revealed)
    assert (0, 0) in cases_revealed


def test_is_end_of_game():
    assert is_end_of_game(3, 3, 2, 7) == True
    assert is_end_of_game(3, 3, 2, 6) == False

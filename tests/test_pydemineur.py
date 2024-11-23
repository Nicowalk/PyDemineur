import pytest
import sys

sys.path.insert(1, "./src")
from pydemineur import create_board, is_end_of_game, reveal_case, is_already_revealed


def test_create_board():
    board, list_of_mines = create_board(4, 4)
    assert len(board) == 4
    assert len(board[0]) == 4
    assert isinstance(list_of_mines, list)


def test_is_end_of_game():
    assert is_end_of_game(4, 4, 2, 14) == True
    assert is_end_of_game(4, 4, 2, 13) == False


def test_reveal_case():
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    cases_revealed = []

    assert reveal_case(0, 0, board, list_of_mines, cases_revealed) == False
    assert reveal_case(0, 2, board, list_of_mines, cases_revealed) == True


def test_is_already_revealed():
    list_of_cases_revealed = [(0, 0), (1, 1)]
    assert is_already_revealed(0, 0, list_of_cases_revealed) == True
    assert is_already_revealed(2, 2, list_of_cases_revealed) == False

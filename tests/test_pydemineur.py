import sys

sys.path.insert(1, "./src")
import pytest
from actions import reveal_cell
from board import create_board
from utilities import (
    is_there_a_mine,
    is_already_revealed,
    reveal_neighbor_0_cells,
    is_end_of_game,
)
from pydemineur import game_run
from unittest.mock import patch


import random


def test_create_board():
    board, list_of_mines = create_board(4, 4)
    assert len(board) == 4
    assert len(board[0]) == 4
    assert isinstance(list_of_mines, list)


def test_is_end_of_game():
    assert is_end_of_game(4, 4, 2, 14) == True
    assert is_end_of_game(4, 4, 2, 13) == False


def test_reveal_cell():
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    cells_revealed = []

    assert reveal_cell(0, 0, board, list_of_mines, cells_revealed) == False
    assert reveal_cell(0, 2, board, list_of_mines, cells_revealed) == True


def test_is_already_revealed():
    list_of_cells_revealed = [(0, 0), (1, 1)]
    assert is_already_revealed(0, 0, list_of_cells_revealed) == True
    assert is_already_revealed(2, 2, list_of_cells_revealed) == False


def test_is_there_a_mine():
    list_of_mines = [(0, 2), (2, 2)]
    assert is_there_a_mine(0, 2, list_of_mines) == True
    assert is_there_a_mine(1, 1, list_of_mines) == False


def test_reveal_neighbor_0_cells():
    board = [[0, 0, -1], [1, 2, 1], [0, 1, -1]]
    cells_revealed = []
    reveal_neighbor_0_cells(0, 0, board, cells_revealed)
    assert (0, 0) in cells_revealed
    assert (0, 1) in cells_revealed
    assert (1, 0) not in cells_revealed
    assert (2, 0) not in cells_revealed


def test_win():
    # I already know the 4x4 board that is created with this seed so I am using it to test
    random.seed(1)
    with patch(
        "builtins.input",
        side_effect=[
            "0",  # action reveal a cell
            "0",  # row
            "0",  # column
            "0",
            "0",
            "3",
            "0",
            "1",
            "1",
            "0",
            "2",
            "1",
            "0",
            "2",
            "3",
            "0",
            "2",
            "2",
            "0",
            "0",
            "1",
        ],
    ):
        assert game_run(4, 4) == 1


def test_lose():
    random.seed(1)
    with patch("builtins.input", side_effect=["0", "0", "2"]):
        assert game_run(4, 4) == 0


def test_annotate_and_lose():
    random.seed(1)
    with patch("builtins.input", side_effect=["1", "0", "2", "0", "0", "2"]):
        assert game_run(4, 4) == 0


def test_already_annotated_and_lose():
    random.seed(1)
    with patch(
        "builtins.input", side_effect=["1", "0", "2", "1", "0", "2", "0", "0", "2"]
    ):
        assert game_run(4, 4) == 0


def test_annotate_revealed_cell_and_lose():
    random.seed(1)
    with patch(
        "builtins.input", side_effect=["0", "0", "0", "1", "0", "0", "0", "0", "2"]
    ):
        assert game_run(4, 4) == 0


def test_reaveal_already_revealed_cell_and_lose():
    random.seed(1)
    with patch(
        "builtins.input", side_effect=["0", "0", "0", "0", "0", "0", "0", "0", "2"]
    ):
        assert game_run(4, 4) == 0

import pytest
import sys

sys.path.insert(1, "./src")
from board import create_board, print_board, print_board_in_game


def test_create_board():
    board, list_of_mines = create_board(3, 3)
    assert len(board) == 3
    assert len(board[0]) == 3
    assert isinstance(list_of_mines, list)


def test_print_board(capsys):
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    print_board(board, list_of_mines)
    captured = capsys.readouterr()
    assert "X" in captured.out


def test_print_board_in_game(capsys):
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    revealed_cases = [(0, 0), (1, 1)]
    annotated_cases = [(2, 2)]
    print_board_in_game(board, list_of_mines, revealed_cases, annotated_cases)
    captured = capsys.readouterr()
    assert "*" in captured.out
    assert "°" in captured.out

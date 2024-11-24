import pytest
import sys

sys.path.insert(1, "./src")
from actions import reveal_cell, action_selection, cell_selection
from unittest.mock import patch


def test_reveal_cell():
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    cells_revealed = []

    assert reveal_cell(0, 0, board, list_of_mines, cells_revealed) == False
    assert reveal_cell(0, 2, board, list_of_mines, cells_revealed) == True


def test_action_selection(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "0")
    assert action_selection() == 0

    monkeypatch.setattr("builtins.input", lambda: "1")
    assert action_selection() == 1

    with patch(
        "builtins.input", side_effect=["0.1", "0"]
    ):
        assert action_selection() == 0
    
    with patch(
        "builtins.input", side_effect=["wrong input", "0"]
    ):
        assert action_selection() == 0

    with patch(
        "builtins.input", side_effect=[" ", "0"]
    ):
        assert action_selection() == 0

    with patch(
        "builtins.input", side_effect=["0.1", "1"]
    ):
        assert action_selection() == 1
    
    with patch(
        "builtins.input", side_effect=["wrong input", "1"]
    ):
        assert action_selection() == 1

    with patch(
        "builtins.input", side_effect=[" ", "1"]
    ):
        assert action_selection() == 1


def test_cell_selection(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "1")
    assert cell_selection(3, 3) == (1, 1)

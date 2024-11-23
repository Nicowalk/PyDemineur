import pytest
import sys

sys.path.insert(1, "./src")
from actions import reveal_case, action_selection, case_selection


def test_reveal_case():
    board = [[0, 1, -1], [1, 2, 1], [0, 1, -1]]
    list_of_mines = [(0, 2), (2, 2)]
    cases_revealed = []

    assert reveal_case(0, 0, board, list_of_mines, cases_revealed) == False
    assert reveal_case(0, 2, board, list_of_mines, cases_revealed) == True


def test_action_selection(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "0")
    assert action_selection() == 0

    monkeypatch.setattr("builtins.input", lambda: "1")
    assert action_selection() == 1


def test_case_selection(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "1")
    assert case_selection(3, 3) == (1, 1)

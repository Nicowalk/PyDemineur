# PyDemineur

PyDemineur is a simple Minesweeper game implemented in Python. This project is designed for educational purposes and correct programming with github.

## Badges

![Test Status](https://github.com/Nicowalk/PyDemineur/actions/workflows/ci.yml/badge.svg)
![Test Status](https://github.com/Nicowalk/PyDemineur/actions/workflows/documentation.yml/badge.svg)
![Coverage Status](https://coveralls.io/repos/github/Nicowalk/PyDemineur/badge.svg?branch=main)

## Documentation

The full documentation can be found here :
https://nicowalk.github.io/PyDemineur/

## Features

- Randomly generated game board with mines
- User interaction to reveal or annotate cells
- Win and lose conditions
- Display of the game board in the terminal
- Choice of the size of the board

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nicowalk/pydemineur.git
    cd PyDemineur
    ```

## Usage

Run the game using the following command:
```sh
python [pydemineur.py](http://_vscodecontentref_/1)
```


Follow the on-screen instructions to play the game. You can choose to reveal a cell or annotate it as a mine.

## Project Structure

src/ </br>
├── actions.py # Functions for user actions (e.g., revealing or annotating cells) </br>
├── board.py # Functions for creating and displaying the game board </br>
├── pydemineur.py # Main game loop and logic </br>
└── utilities.py # Utility functions (e.g., checking for mines, revealing cells)</br>


## How to Play

1. The game starts by displaying the initial game board.
2. You will be prompted to choose between:
   - Revealing a cell.
   - Annotating a cell as a mine.
3. Enter the row and column numbers to select a cell.
4. The game will update the board and check for win or lose conditions:
   - **Win**: Reveal all non-mine cells.
   - **Lose**: Reveal a mine.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
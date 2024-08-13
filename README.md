# Catch The Turtle Game

CatchTheTurtle is an interactive `Python` game that uses the `turtle` graphics library. In this game, the player must click on randomly appearing turtles to score points. The game features a grid of turtles that randomly appear on the screen for a limited time. The player's goal is to click on as many turtles as possible before time runs out.

## Installation

1. Clone the repository:
```
git clone https://github.com/sleinkaraman/CatchTheTurtle.git
```

2. Navigate to the project directory:
```
cd CatchTheTurtle
```

## Usage

To start the game, simply run the CatchTheTurtle.py script using Python:
```
python CatchTheTurtle.py
```

## How to Play

- The game grid consists of 25 turtle objects arranged in a 5x5 pattern.
- Turtles are hidden by default and appear one at a time at random locations on the grid.
- The player gains one point for each successful turtle click.
- The game lasts for 10 seconds, and the final score is displayed when the time is up.

## Code Structure

- `setupScore()`: Initializes and displays the score at the top of the screen.
- `makeTurtle(x, y)`: Creates and positions turtles on the grid, and defines the click event for scoring.
- `setupTurtles()`: Sets up the grid of turtles.
- `hideTurtles()`: Hides all turtles.
- `showTurtles()`: Randomly shows a turtle on the screen for the player to click.
- `countdown(time)`: Manages the countdown timer and displays the remaining time. Ends the game when the timer reaches zero.

## Contributing

Contributions are welcome! If you have suggestions or want to improve the code, feel free to fork the repository and create a pull request.







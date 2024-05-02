# Welcome to Tic tac Toe

This classic game is a simple way to test your strategic skills against an AI, also known as Computer. Can you win over Computer?

## Table of contents

* User Experience (UX)
* Strategy Plane
* Scope Plane
* Structure Plane
* Skeleton Plane
* Surface Plane
* Features
* Technologies
* Testing
* Test Results & Bugs
* Test Results & Bugs
* Deployment
* Credits

## Project Goals
* **Test strategic thinking**: The primary goal is for the player to test their strategic thinking against an AI opponent.
* **Have fun**: As a game, I want it to be enjoyable for the user.
* **User-friendliness**: Provide a user-friendly interface that is easy to understand.

## Target Audience
* **Individuals**: The target audience includes people who seek to pass the time and enjoy challenging their thinking.
* **Curious**: The secondary target audience comprises individuals who are unfamiliar with console games and are curious about playing against an AI.

## User Stories

I want to have a fun and casual gaming experience and test my strategic thinking against an AI opponent:

**Starting the Game**:
  * When I open the Tic Tac Toe application, I can choose the size of the board I want to play on.

**Game Interface**:
  * Once I select the board size, I am presented with the game board, which consists of the grid size I selected.
  * The board is visually appealing and easy to understand, with clearly marked squares for placing my moves ('X') and the AI's moves ('O').

**Making Moves**:
  * During my turn, I can first select the row and then the column where I want to place my move.
  * I make my move, the AI makes its move automatically.

**Gameplay**:
  * The AI opponent provides a challenge, using the Minimax algorithm to make its moves.
  * I can see indicators of whose turn it is during the game, ensuring smooth gameplay.

**Winning and Losing**:
  * If I manage to get three, four, or five (depending on the board size) of my symbols ('X') in a row (horizontally, vertically, or diagonally), I win the game.
  * If the AI gets three, four, or five (depending on the board size) of its symbols ('O') in a row, I lose the game.
  * The game ends in a draw if the board is filled with symbols and no player wins.

**Ending the Game**:
  * After the game ends, I am presented with an option to start a new game.

**Accessibility and User-Friendliness**:
  * The user interface is intuitive and easy to navigate, providing a pleasant gaming experience for players of all levels.


### Strategy Plane

### Site Goals**

### User Stories**

### Scope Plane

## Features planned

Got it! Here's the revised list with the addition:

* Implement a maximum width of 1750px.
* Ensure responsiveness across all pages, meaning the layout adjusts accordingly.
* Include an "About" page that explains the purpose of this game.
* Allow the user to choose to play on three, four, or five rows.
* Provide a help command line for the user.
* Enable the user to restart the game with a button.
* Enable user gameplay against AI.
* Add a Tic Tac Toe game.
* Incorporate a command line for users to play on.

### Structure Plane

### Skeleton Plane

### Surface Plane

## Wireframes**

### Wireframes / Site Design

## Design

### Color schemes

## Typography

## Graphics/Imagery

### Design changes

* I made a change to the design after creating the initial wireframe and consulting with my mentor, who clarified that a complete user interface wasn't necessary. Following that discussion, I simplified the interface and adapted it to be more terminal-based.

## Features

## All Pages

### All Pages - Features - Details & Description**

## Credits

### Code

### Images and text

### README

* The structure of this README was drawn from [emmahewsons "SWIMMÔN Wild Swimming Events Website"](https://github.com/emmahewson/mp3-swimmon?tab=readme-ov-file#Credits) and served as a reference my README

### Acknowledgements

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

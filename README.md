# int-1-1-othello

After working on my previous project idea over the last few days, I realized the project was a bit more ambitious than I had initially realized. So I decided to work on a fun project using turtle graphics for python3.x. In an abstract sense, it implements CRUD by creating pieces at new squares, reading them to display the score, updating them when the opponent moves to the right square, and effectively deleting them when the game is relaunched and can be played again. At the core of this project, though, was my desire to make a simple application that was entertaining, elegant, and functional.

## Getting Started

Learn or refresh your memory on how to play othello (https://www.wikihow.com/Play-Othello), then run the application using python3.

## Code Structure and Design

The turtle graphics module relies on a 2D coordinate plain, with the upper left being (0,0). My application attempts to abstract various gameplay elements as much as possible, using coordinates as only the most base-level logic. The most challenging part of this project was building the sandwich function, which recursively determines which other pieces to flip by going down each sequence of adjacent pieces (vertically, horizontally and diagonally) and determining whether it fits the criteria for converting them (whether or not it 'sandwiches' the opposing color's pieces). I began to add some elements that could allow the user to play against the computer, but did not have time to implement this functionality. Regardless, the application is functional as a 2-player game.

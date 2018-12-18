# PolyChess

PolyChess (named polychess as Git repository) is a Chess engine written in Python and used as practicals for a course on project management at the engineering school Polytech Annecy-Chambéry. 

The aim of this repository is not to provide any complete Chess engine since students have to do it based on python-chess. As a consequence, persons interested in this project should check the different forks.

The required features for PolyChess are: 

* PolyChess is able to play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess

## Milestones for the project

Milestone 1:

PolyChess is able to play against user or another engine through UCI, has an opening book and an AI

Milestone 2:

PolyChess plays on Lichess (and FICS) 

Milestone 3:

Board representation and legal moves are no longer provided by python-chess but are students' responsibilities

## New techniques/skills/terms to get acquainted with

* Chess (maybe)
* Universal Chess Interface (UCI) (http://wbec-ridderkerk.nl/html/UCIProtocol.html)
* Portable General Notation (PGN)
* Board representation (bitboards, 0x88, 120-square representation, 64-square representation)
* MinMax (Negamax)
* Alpha-Beta pruning
* Chess rules (five fold repetition, seventy-five moves)
* Opening book (Polyglot)
* Forsyth-Edwards Notation (FEN) (https://www.chessprogramming.org/Forsyth-Edwards_Notation)
* Piece-Square table
* Move ordering
* Position evaluation
* Transposition table
* Zobrist key
* Perft

## Running

To run this chess game, you have to run the file "main.py". 

/!\/!\/!\ Be carefull about the repository access where you want to save the games. /!\/!\/!\

After that you will have to :
* Fill the event name (string)
* Fill the site where the event takes place (string)
* Fill the round number (integer)
* Fill the number 1 player name (string)
* Fill the number 2 player name (string)
* Choose a game type (IAvsIA, PlayerVsIa, PlayerVsPlayer)

The game will run and be save in "savedGames.pgn" file, which you can edit with a text editor.

### Trello invite link
https://trello.com/invite/b/EzclDVXL/f24c3069c9a6f61eb6ff34cb8334eb3f/tp2%C3%A06


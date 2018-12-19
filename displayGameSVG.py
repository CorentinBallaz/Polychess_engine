import chess
import chess.svg
from IPython.display import SVG,display

#This program allow us to display a chess game (display the board)

board=chess.Board()
display(SVG(chess.svg.board(board=board)))

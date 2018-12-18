import chess
import chess.svg
from IPython.display import SVG

display(SVG(chess.svg.piece(chess.Piece.from_symbol("Q"))))

board=chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
squares=board.attacks(chess.E4)
display(SVG(chess.svg.board(board=board)))

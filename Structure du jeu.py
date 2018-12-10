# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:35:47 2018

@author: Théo
"""
#Setup
import chess
import chess.polyglot


board = chess.Board()
print(board)



#Main
while not(board.is_game_over()):
        moves = board.legal_moves
        if best_move(board) in moves:
            board.push(best_move(board))
            print(board)
            
        if board.is_game_over():
            print("The game is over")
            print(board.result())
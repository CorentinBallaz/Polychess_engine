# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:23:30 2018

@author: Théo
"""
#Setup
import chess
import chess.polyglot


board = chess.Board()
print(board)


#Best_move fct
def best_move(board):
    liste_coup=[]

    with chess.polyglot.open_reader("bookfish.bin") as reader:
    
        for entry in reader.find_all(board):
            liste_coup.append([entry.move(), entry.weight, entry.learn])
    
        #extraction du meilleure coup de la liste des coups viables
        puissance = 0
        indice = 0
        for i in range (len(liste_coup)):
            if liste_coup[i][1] > puissance :
                indice = i
                puissance = liste_coup[i][1]
        print(liste_coup)
        return liste_coup[indice][0]

        
        


#Structure de jeu en IA VS IA
while not(board.is_game_over()):
        moves = board.legal_moves
        #On commence par chercher le best move dans polyglot
        if best_move(board) in moves:
            board.push(best_move(board))
            print(board)
        #Si il n'y est pas on utilise min/max 
         
        #
        
        #Si la partie est fini on affiche le résultat
        if board.is_game_over():
            print("The game is over")
            print(board.result())
    


             
        
        
        
        
        
        
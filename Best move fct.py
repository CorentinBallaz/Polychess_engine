# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:14:35 2018

@author: Théo
"""
#Setup

import chess
import chess.polyglot


board = chess.Board()
print(board)



#Main
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
        
        
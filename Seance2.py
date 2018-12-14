# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:23:30 2018

@author: Théo
"""



#### Setup ####
import chess
import chess.polyglot
### Import pgn and datetime module ###
import chess.pgn
import datetime
game=chess.pgn.Game()



#### Add game Tag informations ####
def game_tag_info ():
    game.headers["Event"]=input("nom de l'évènement : ")
    game.headers["Site"]=input("nom du site : ")
    game.headers["Date"]=datetime.datetime.now()
    game.headers["Round"]=input("round number : ")
    game.headers["White"]=input("nom du joueur 1 : ")
    game.headers["Black"]=input("nom du joueur 2 : ")



####Best_move fct with PolyGlot selection ####
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

        
        

#### Structure de jeu en IA VS IA ####
def IAvsIA ():        

    board = chess.Board()
    print(board)

    while not(board.is_game_over()):
            moves = board.legal_moves
            #On commence par chercher le best move dans polyglot
            if best_move(board) in moves:
                board.push(best_move(board))
                game.add_variation(best_move(board))
                print(board)
                #Si il n'y est pas on utilise min/max 
                
                #
                
                #Si la partie est fini on affiche le résultat
                if board.is_game_over():
                    print("The game is over")
                    print(board.result())
    




#### Structure de jeu en MAN VS IA ####
def MANvsIA ():

    board = chess.Board()
    print(board)
    
    while not(board.is_game_over()):
            moves = board.legal_moves
            #Le joueur commence toujours
            man_move =chess.Move.from_uci(input("départ arrivée : "))
            if man_move in moves :
                board.push(man_move)
                game.add_variation(man_move)
            else:
                while man_move not in moves :
                    print("ce mouvement n'est pas possible, veuillez en saisir un autre")
                    man_move =input("départ arrivée : ")
                    board.push(man_move)
                    game.add_variation(man_move)
                        
    
            moves = board.legal_moves
            #On commence par chercher le best move dans polyglot
            if best_move(board) in moves:
                board.push(best_move(board))
                game.add_variation(best_move(board))
                print(board)
                #Si il n'y est pas on utilise min/max 
         
            #
            
            #Si la partie est fini on affiche le résultat
            if board.is_game_over():
                print("The game is over")
                print(board.result())
         
            


#### Structure de jeu en MAN VS MAN ####
def MANvsMAN ():
    
    board = chess.Board()
    print(board)
    
    while not(board.is_game_over()):
            moves = board.legal_moves
            #On demande la case départ et d'arrivée
            man_move =chess.Move.from_uci(input("départ arrivée : "))
            
            #On vérifie si le mouvment est possible
            if man_move in moves :
                board.push(man_move)
                game.add_variation(man_move)
                print(board.fen())
                print(board)
            #Si il ne l'est pas, on refait la demande en affichant la liste des mouvements possible
            else:
                while man_move not in moves :
                    print("ce mouvement n'est pas possible, veuillez en saisir un autre")
                    print("Voici la liste des mouvements possibles")
                    for move in board.legal_moves:
                        print(move) 
                        man_move =chess.Move.from_uci(input("départ arrivée : "))
                        board.push(man_move)
                        game.add_variation(man_move)
                        print(board)
                            
                        #Si la partie est fini on affiche le résultat
                        if board.is_game_over():
                            print("The game is over")
                            print(board.result())
                                
                                
#### Choix du mode de jeu ####                                
funcmap = {1 : IAvsIA, 2 : MANvsIA, 3 : MANvsMAN}    
                            
def choix_mode (mode):
        funcmap[mode]()
        
        
        
        
#### Lancement de la partie ####
print(game_tag_info())
print("veuillez choisir le mode de jeu")
print("1 pour IAvsIA")
print("2 pour MANvsIA")
print("3 pour MANvsMAN")
print(choix_mode(int(input("mode : "))))



####Enregistrement de la partie ####
new_pgn=open("C:/Users/Théo/Documents/Cours/S5/PROJ531 - Gestion de projets/TP2 à 6/polychess-master/polychess/savedGames.pgn","a",encoding="utf-8")
exporter=chess.pgn.FileExporter(new_pgn)
game.accept(exporter)

new_pgn.close()


    
                                
                                
        

             
        
        
        
        
        
        
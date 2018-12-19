# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:23:30 2018
@author: Théo
"""



#### Setup ####
import chess
import chess.polyglot
### Import pgn and datetime module, setup PGN saving ###
import chess.pgn
import datetime
game=chess.pgn.Game()
line = []
####Import Random for random move####
import random

#### Add game Tag informations ####
def game_tag_info ():
    game.headers["Event"]=input("nom de l'évènement : ")
    game.headers["Site"]=input("nom du site : ")
    game.headers["Date"]=datetime.datetime.now()
    game.headers["Round"]=input("numéro du round : ")
    game.headers["White"]=input("nom du joueur 1, WHITE : ")
    game.headers["Black"]=input("nom du joueur 2, BLACK : ")



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
        if liste_coup ==[]:
            return "Nothing"
        else:
            return liste_coup[indice][0]

        
        

#### Structure de jeu en IA VS IA ####
def IAvsIA ():        

    board = chess.Board()
    print(board)
    print("")
    while not(board.is_game_over()):
        moves = board.legal_moves

            #On commence par regarder si il y a un best_move venant de polyglot
            #Si il n'y en a pas on utilise min/max ou aleatory
        if best_move(board) == "Nothing" :
            list_move=[]
            #moves n'est pas indexable, donc on ajoute chaque move dans une liste
            for move in moves:
                    list_move.append(move)
            #on sélectionne un move au hasard de la liste et on le push        
            rand_int = random.randint(0,len(list_move)-1)
            line.append(list_move[rand_int])
            board.push(list_move[rand_int])
            print(board)
            print("")
            #Si il y a un best move on le push
        elif best_move(board) in moves:
            moveToPush = best_move(board)
            line.append(moveToPush)
            board.push(moveToPush)
            print(moveToPush)         
            print(board)
            print("")
        else:
            print("*****************  ERREUR ***********************")
 
        #Si la partie est fini on affiche le résultat
        if board.is_game_over():
            print("The game is over")
            print(board.result())
            game.headers["Result"]=board.result()
            
    game.add_line(line)
    new_pgn=open("C:/Users/Théo/Documents/Cours/S5/PROJ531-Gestion-de-projets/TP2-à-6/polychess-master/polychess/savedGames3.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
 

   



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
                line.append(man_move)
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
                        
            #c'est désormais au tour de l'IA
            
            moves = board.legal_moves
            #On commence par regarder si il y a un best_move venant de polyglot
            #Si il n'y en a pas on utilise min/max ou aleatory
            if best_move(board) == None :
                list_move=[]

                #moves n'est pas indexable, donc on ajoute chaque move dans une liste
                for move in moves:
                        list_move.append(move)
                #on sélectionne un move au hasard de la liste et on le push        
                rand_int = random.randint(0,len(list_move)-1)
                board.push(list_move[rand_int])
                line.append(list_move[rand_int])
                print(board)
            
            elif best_move(board) in moves:
                board.push(best_move(board))
                line.append(best_move(board))
                print(board)
                
            #Si la partie est fini on affiche le résultat
            if board.is_game_over():
                print("The game is over")
                print(board.result())
                game.headers["Result"]=board.result()
                
    ####Enregistrement de la partie ####
    game.add_line(line)
    new_pgn=open("C:/Users/Théo/Documents/Cours/S5/PROJ531-Gestion-de-projets/TP2-à-6/polychess-master/polychess/savedGames3.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
         
            


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
                game.headers["Result"]=board.result()
                
    ####Enregistrement de la partie ####
    new_pgn=open("C:/Users/Théo/Documents/Cours/S5/PROJ531-Gestion-de-projets/TP2-à-6/polychess-master/polychess/savedGames3.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
                                
                                
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






    
                                
                                
        

             
        
        
        
        
        
        
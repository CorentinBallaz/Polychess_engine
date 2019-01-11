# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:23:30 2018
@author: Théo HENAFF,Tanguy MARITON, Corentin BALLAZ, William BURILLON
"""



#### Setup ####
import chess
import chess.polyglot

### Import pgn and datetime module, setup PGN saving ###
import chess.pgn
import datetime
from MinMax import MinMax
game=chess.pgn.Game()
line = []

####Import svg and IPython for SVG display####
import chess.svg
from IPython.display import SVG,display



#### Add game Tag informations ####
'''
Initialization of the game for PGN saving
'''

def game_tag_info ():
    game.headers["Event"]=input("nom de l'évènement : ")
    game.headers["Site"]=input("nom du site : ")
    game.headers["Date"]=datetime.datetime.now()
    game.headers["Round"]=input("numéro du round : ")
    game.headers["White"]=input("nom du joueur 1, WHITE : ")
    game.headers["Black"]=input("nom du joueur 2, BLACK : ")




####Best_move fct with PolyGlot selection ####
'''
This function will look for the best move if the board is in a library
called bookfish.bin
if the board isn't in book fish it will return the string 'nothing'
'''

def best_move(board):
    liste_coup=[]

    with chess.polyglot.open_reader("bookfish.bin") as reader:
    
        for entry in reader.find_all(board):
            liste_coup.append([entry.move(), entry.weight, entry.learn])
    
        #extraction of the best move from the list of 
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

        
        

#### IA vs IA game part ####
'''   
The IA will  first look for polyglot move but if there's no move available from 
the bookfish it will use alpha-beta research, an optimized version of min-max method
'''
         
def IAvsIA ():        
    board = chess.Board()
    display(SVG(chess.svg.board(board=board)))
    print("")
    while not(board.is_game_over()):
        moves = board.legal_moves

            #It look if the best_move function has a move to push
            #If not, we use alpha-beta method
        if best_move(board) == "Nothing" :
            
            move=MinMax.minimaxRoot(3,board,True)
            line.append(move)
            board.push(move)
            display(SVG(chess.svg.board(board=board, lastmove = move)))            
            print("")
            #If there is a move from polyglot, we push it
        elif best_move(board) in moves:
            moveToPush = best_move(board)
            line.append(moveToPush)
            board.push(moveToPush)
            display(SVG(chess.svg.board(board=board, lastmove = moveToPush)))            
            print("")

 
        #We look after every move if the game is over in order to end it
        if board.is_game_over():
            print("The game is over")
            print(board.result())
            game.headers["Result"]=board.result()
            
            
    ###Game saving ###        
    game.add_line(line)
    new_pgn=open("D:/Polytech/FI 3/Proj/gitTheo2.0/savedGames.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
 

 
    
#### MAN vs IA game part ####
def MANvsIA ():

    board = chess.Board()
    display(SVG(chess.svg.board(board=board)))
    
    while not(board.is_game_over()):
            moves = board.legal_moves
            #The MAN start everytime
            man_move =chess.Move.from_uci(input("your move : "))
            if man_move in moves :
                board.push(man_move)
                line.append(man_move)
                display(SVG(chess.svg.board(board=board, lastmove = man_move)))            
            else:
                while man_move not in moves :
                    print("Illegal move, please try an other one")
                    print("Here is the list of legal move")
                    for move in board.legal_moves:
                        print(move) 
                    man_move =chess.Move.from_uci(input("your move : "))
                board.push(man_move)
                line.append(man_move)
                display(SVG(chess.svg.board(board=board, lastmove = man_move)))            
                    
        #We look after every move if the game is over in order to end it
            if board.is_game_over():
                print("The game is over")
                print(board.result())
                game.headers["Result"]=board.result()                
                print("")                 
                
                
            #Now it's IA turns
            
            moves = board.legal_moves
    
                #It look if the best_move function has a move to push
                #If not, we use alpha-beta method
            if best_move(board) == "Nothing" :
                
                move=MinMax.minimaxRoot(3,board,True)
                line.append(move)
                board.push(move)
                display(SVG(chess.svg.board(board=board, lastmove = move)))            
                print("")
                #If there is a move from polyglot, we push it
            elif best_move(board) in moves:
                moveToPush = best_move(board)
                line.append(moveToPush)
                board.push(moveToPush)
                display(SVG(chess.svg.board(board=board, lastmove = moveToPush)))            
                print("")

 
            #We look after every move if the game is over in order to end it
            if board.is_game_over():
                print("The game is over")
                print(board.result())
                game.headers["Result"]=board.result()                
                print("")      

                
    ###Game saving ###        
    game.add_line(line)
    new_pgn=open("D:/Polytech/FI 3/Proj/gitTheo2.0/savedGames.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
         
            


#### Structure de jeu en MAN VS MAN ####
def MANvsMAN ():
    
    board = chess.Board()
    display(SVG(chess.svg.board(board=board)))
    
    while not(board.is_game_over()):
            moves = board.legal_moves
            #The MAN start everytime
            man_move =chess.Move.from_uci(input("your move : "))
            if man_move in moves :
                board.push(man_move)
                line.append(man_move)
                display(SVG(chess.svg.board(board=board, lastmove = man_move)))            
            else:
                while man_move not in moves :
                    print("Illegal move, please try an other one")
                    print("Here is the list of legal move")
                    for move in board.legal_moves:
                        print(move) 
                    man_move =chess.Move.from_uci(input("your move : "))
                board.push(man_move)
                line.append(man_move)
                display(SVG(chess.svg.board(board=board, lastmove = man_move)))            
                    
            #We look after every move if the game is over in order to end it
            if board.is_game_over():
                print("The game is over")
                print(board.result())
                game.headers["Result"]=board.result()                
                print("")                          
            

                
    ###Game saving ###        
    game.add_line(line)
    new_pgn=open("D:/Polytech/FI 3/Proj/gitTheo2.0/savedGames.pgn","a",encoding="utf-8")
    exporter=chess.pgn.FileExporter(new_pgn)
    game.accept(exporter)
    
    new_pgn.close()
                                
      

                          
#### Gamemode ####                                
funcmap = {1 : IAvsIA, 2 : MANvsIA, 3 : MANvsMAN}    
                            
def choix_mode (mode):
        funcmap[mode]()
        
        
        
        
#### Game launching ####
print(game_tag_info())
print("veuillez choisir le mode de jeu")
print("1 pour IAvsIA")
print("2 pour MANvsIA")
print("3 pour MANvsMAN")
print(choix_mode(int(input("mode : "))))

####For PGN save test : Mat du lion : g2g4-e7e5-f2f3-d8h4####





    
                                
                                
        

             
        
        
        
        
        
        
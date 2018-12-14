


"""
Fonctionnement de base pour enregistrer une partie d'échec dans un fichier PGN, avec les tags et les déplacements.
"""

#### Import pgn and datetime module ####

import chess.pgn
import datetime
game=chess.pgn.Game()

#### Add game Tag informations ####

game.headers["Event"]="Tournoi Polytech"
game.headers["Site"]="Annecy"
game.headers["Date"]=datetime.datetime.now()
game.headers["Round"]="8"
game.headers["White"]="Bourillon"
game.headers["Black"]="Blz"

#### Add the game deplacements ####

game.add_variation(chess.Move.from_uci("e2e4"))

#### Append the game in the pgn file ####

new_pgn=open("E:/PROJ531/PolyChess/savedGames.pgn","a",encoding="utf-8")
exporter=chess.pgn.FileExporter(new_pgn)
game.accept(exporter)

new_pgn.close()


#Print the 1st game of the file, we can look further for printing the last game

#pgnFile=open("E:/PROJ531/PolyChess/savedGames.pgn","r")
#firstGame=chess.pgn.read_game(pgnFile)
#print(firstGame)
#
#pgnFile.close()
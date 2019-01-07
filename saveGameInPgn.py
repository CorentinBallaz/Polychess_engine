


"""
Fonctionnement de base pour voir comment enregistrer des éléments d'une partie d'échec dans un fichier PGN : tags et déplacements.
"""

#### Import pgn and datetime module ####

import chess.pgn
import datetime

#### Init game ####

game=chess.pgn.Game()

#### Add game Tag informations ####

game.headers["Event"]="Tournoi Polytech"
game.headers["Site"]="Annecy"
game.headers["Date"]=datetime.datetime.now()
game.headers["Round"]="8"
game.headers["White"]="Bourillon"
game.headers["Black"]="Blz"

#### Add a move in a pgn file (here savedGames.pgn) ####
line=[]
move=chess.Move.from_uci("e1e4") #Exemple
line.append(move)
game.add_line(line)
pgnFile=open("E:/PROJ531/PolyChess07/savedGames.pgn","a",encoding="utf-8")
exporter=chess.pgn.FileExporter(pgnFile)
game.accept(exporter)
pgnFile.close()
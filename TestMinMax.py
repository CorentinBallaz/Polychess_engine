# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:43:30 2018

@author: burillow
"""



def minMax(board,prof,currentPlayer):
   
#    
#   listCoup=getAvailableMove(board)
#   for i in range(0,len(listCoup)):
        
        if prof==0:
            
        

            return boardValue(board)
        movPoss = getAvailableMove(board)
        if currentPlayer:
            value = -9999
            for i in range(0,len(movPoss)):
                newBoard=board.push(movPoss[i])
                value=maxi(value,minMax(newBoard,prof-1,False))
                return value
        else:
            value=9999
            for i in range(0,len(movPoss)):
                newBoard=board.push(movPoss[i])
                value=mini(value,minMax(newBoard,prof-1,True))
                return value
            
                
                            
#def maxi(currentValue,)        
    

   


def boardValue(board):
    """
    Evaluation function wich return the value of a board, this evaluation function is just an Alpha-version
    """
        
    
    return int(whiteBoardValue(board)-blackBoardValue(board))



def blackBoardValue(board):
    
    resTemp=[]
    i=0
    while board.fen()[i]!= (' '):
        resTemp.append(board.fen()[i])
        i=i+1
    blackValue=0.0
    for i in range(0, len(resTemp)):
        
        if resTemp[i]=='p':
            blackValue=blackValue+1.0
        elif resTemp[i]=='r':
            blackValue= blackValue+ 5.1
        elif resTemp[i]== 'n':
            blackValue= blackValue+3.2
        elif resTemp[i]=='b':
            blackValue= blackValue+3.33
        elif resTemp[i]=='q':
            blackValue=blackValue+8.8
            
    return round(blackValue)

def whiteBoardValue(board):
    
    resTemp=[]
    i=0
    while board.fen()[i]!= (' '):
        resTemp.append(board.fen()[i])
        i=i+1
    whiteValue=0.0
    for i in range(0, len(resTemp)):
        
        if resTemp[i]=='P':
            whiteValue=whiteValue+1.0
        elif resTemp[i]=='R':
            whiteValue= whiteValue+ 5.1
        elif resTemp[i]== 'N':
            whiteValue= whiteValue+3.2
        elif resTemp[i]=='B':
            whiteValue= whiteValue+3.33
        elif resTemp[i]=='Q':
            whiteValue=whiteValue+8.8
            
    return round(whiteValue)


def getAvailableMove(board):
    """
    Function which allows us to get the legal Moves of a board
    """
    resMove=[]
    moves = board.legal_moves
    for move in moves :
        resMove.append(str(move))
    
    return resMove


            
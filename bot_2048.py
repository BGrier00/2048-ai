"""
Python 2048 Game : Basic Console Based User Interface For Game Play

Originally written by Phil Rodgers, University of Strathclyde

AI written by 
"""

from py2048_classes import Board, Tile
import time
import math
import random

from copy import deepcopy 

def getMove(board):
    if len(board.empty()) == 0: move = expectiMinimaxValue(board, 3, 0)             # 3
    elif len(board.empty()) <= 3: move = expectiMinimaxValue(board, 5, 0)           # 5
    elif len(board.empty()) >= 10: move = expectiMinimaxValue(board, 2, 0)          # 2
    else: move = expectiMinimaxValue(board, 3, 0)                                   # 3
    if type(move) == int: return move
    return move



def expectiMinimaxValue(state, d, turn):          # turn 0: Players turn, turn1: Computers Turn
    if turn == 0:
        maxValTuple = maxValue(state, d)
        return maxValTuple[1]
    if turn == 1:
        return chanceValue(state, d)
    


def maxValue(state, d):         # returns the maximised score of all nextStates()
    if len(state.possible_moves()) == 0:
        return 0, "UP"
    if d == 0: return eva(state)
    v = -math.inf
    bestMove = "UP"
    for s in state.possible_moves():
        boardCopy = deepcopy(state)
        boardCopy.make_move(s)
        expextTup = (chanceValue(boardCopy, d-1))
        if expextTup > v:
            v = expextTup
            bestMove = s
    return v, bestMove


def chanceValue(state, d):     
    if d == 0: return eva(state)
    v = 0
    noOfPossibilities = len(state.empty())
    for eachEmpty in state.empty():     # eachEmpty = tuple with X, Y co ordinates
        newState2 = deepcopy(state)
        newState2.grid[eachEmpty[1]][eachEmpty[0]] = Tile(1)
        maxValOf2 = (maxValue(newState2, d-1))  # tuple is returned with val in 0th index
        newState2.grid[eachEmpty[1]][eachEmpty[0]] = Tile(2)
        maxValOf4 = (maxValue(newState2, d-1))  # tuple "   "         "   "   "  "    "
        if type(maxValOf2) == int and type(maxValOf4) == int: v = v + (0.8 * maxValOf2) + (0.2 * maxValOf4)
        else : v = v + (0.8 * maxValOf2[0])/noOfPossibilities  + (0.2 * maxValOf4[0])/noOfPossibilities 
    return v


def terminal(state):
    emptyPos = state.empty()
    if len(emptyPos) == 0 and state.possible_moves() == []:     # no more moves
        return True
    else:
        return False

def eva(state):         # the most important function! uses snake heuristics to determine where to place next 
    emptyPos = state.empty()
    noEmptyTiles = len(emptyPos)
    
    weight2=[[pow(2,15),pow(2,14),pow(2,8),pow(2,4)],      ## all changed from 4, double the power numbers
            [pow(2,1),pow(2,1),pow(2,1),pow(2,1)],
            [pow(2,1),pow(2,1),pow(2,1),pow(2,1)],
            [pow(2,1),pow(2,1),pow(2,1),pow(2,1)]] # snake grid
    
    weight=[[pow(4,30),pow(4,28),pow(4,26),pow(4,24)],      ## all changed from 4, doubled the power numbers
            [pow(4,16),pow(4,18),pow(4,20),pow(4,22)],
            [pow(4,14),pow(4,12),pow(4,10),pow(4,8)],
            [pow(2,0),pow(2,2),pow(2,4),pow(2,6)]] # snake grid
    score = 0
    penalty = 0
    for row_idx, row in enumerate(state.grid):
        for tile_idx, tile in enumerate(row):
                if tile is not None:
                    tileVal = tile.get_tile_value()     # just tile instead of tileValue ######
                    tileWeight = weight[row_idx][tile_idx]
                    tileWeight2 = weight[row_idx][tile_idx]
                    score = score + (tileVal * tileWeight)
                    if row_idx == 1 or row_idx == 2 and tile_idx == 1 and tile_idx == 2:
                        penalty = penalty + tileVal     # tileVal
    return int(score)

def main():
    board = Board()
    board.add_random_tiles(2)
    print("main code")

    move_counter = 0
    move = None
    move_result = False
    
    
    overalltime=time.time()
    while True:
        print(board)
        print("Number of successful moves:{}, Last move attempted:{}:, Move status:{}".format(move_counter, move, move_result))
        if board.possible_moves()==[]:
            if (board.get_max_tile()[0]<2048):
                print("You lost!")
            else:
                print("Congratulations - you won!")
            break
        begin = time.time()
        move = getMove(board)
        move_result = board.make_move(move)
        

        
######################################  Do not modify 4 lines below  ######################################
        print("Move time: ", time.time()-begin)
        board.add_random_tiles(1)
        move_counter = move_counter + 1
    print("Average time per move:", (time.time()-overalltime)/move_counter)
    

if __name__ == "__main__":
    main()

  


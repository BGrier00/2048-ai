# 2048-ai
A bot designed for the popular game '2048' which implements Monte Carlo tree searches to make intelligent decisions.

Bot AI designed during 3rd year of undergraduate studies @ UoStrath. 
Game template provided by Phil Rodgers for work in CS-310, 'Foundations of Artificial Intelligence'. 

## Overview 
To launch the bot, you simply need to run the bot_2048.py file.

A very basic console based user interface is presented, and will print after each turn. For example:

```
-------------------------------------
|  512   |  128   |   64   |   32   |
-------------------------------------
|   4    |   16   |   32   |   16   |
-------------------------------------
|        |        |   8    |   2    |
-------------------------------------
|        |        |   4    |        |
-------------------------------------
Number of successful moves:336, Last move attempted:UP:, Move status:True
Move time:  0.027596712112426758
Score:5276, Merge count:327, Max tile:512, Max tile coords:(1,1)
```

The bot will continue to make moves until each tile is filled and no further moves can be made. Example end game output:

```
-------------------------------------
|  4096  |  1024  |   4    |   2    |
-------------------------------------
|   32   |   64   |  512   |  256   |
-------------------------------------
|   8    |   16   |   32   |   64   |
-------------------------------------
|   4    |   2    |   4    |   16   |
-------------------------------------
Number of successful moves:2582, Last move attempted:RIGHT:, Move status:True
Move time:  0.0019953250885009766
Score:59244, Merge count:2568, Max tile:4096, Max tile coords:(1,1)
Congratulations - you won!
Average time per move: 0.1374833669706798
```

## Performance 
A number of methods were employed to increase the overall score and the "snake heuristic" resulted in the best performance. This will ensure higher-value tiles are 'pushed' to the corners of each game. 

Bot will almost always succeed in reaching at least one tile valuing 2048. The bot will continue to play beyond this.
Score averages ~50,000.
Time averages ~0.1 seconds per move. 

Final grade for this submission was 85% (First-class). 




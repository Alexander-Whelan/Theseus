#Theseus testing

from theseus import createmaze
from theseus import Theseus

#Sample maze
XOXXXX
XOXOOX
XOXOXX
XOOOSX
XXXXXX

maze = createmaze()
Theseus(maze)

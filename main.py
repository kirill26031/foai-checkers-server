import sys
import threading

from checkers.game import Game

from backend.server import main

threading.Thread(target=main, args=(sys.argv[1:],)).start()

game = Game()
print(game.whose_turn())

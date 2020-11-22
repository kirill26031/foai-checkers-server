from checkers.game import Game
from board_drawing import BDManager

## Init components
game = Game()
uiManager = BDManager(game=game)

## Main
# TODO: start server and move this to server
# WARN: This is for test purposes only
# sleep(5)
game.move([9, 13])
uiManager.setNeedsUpdate()
print("move done")
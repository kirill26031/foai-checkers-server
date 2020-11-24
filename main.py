import sys
import threading

from checkers.game import Game

game = Game()


def start_server():
    from backend.server import main

    threading.Thread(target=main, args=(sys.argv[1:],)).start()


if __name__ == '__main__':
    print(game.whose_turn())
    start_server()

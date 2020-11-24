import sys
import threading

from checkers.game import Game

game = Game()


def start_server():
    from backend.server import main

    threading.Thread(target=main, args=(sys.argv[1:],)).start()


def test_server(rand_sleep=False):
    from api_tester import ApiTester

    ApiTester(rand_sleep=rand_sleep).start_test()


if __name__ == '__main__':
    start_server()
    # test_server(True)  # uncomment this line to run API Tester

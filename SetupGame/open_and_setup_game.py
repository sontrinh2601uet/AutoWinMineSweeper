# Created by Sown_Moon
# Project: AutoWinMineSweeper
# Date: 08-Nov-20
# Class: open_and_setup_game.py
"""Definition for open_and_setup_game"""
import win32con
import win32gui
from pywinauto import application


from Constants import PATH_TO_GAME


class SetUp:

    mine_sweeper = None

    def __init__(self):
        # self.open_game()
        self.set_up_game()

    # def open_game(self):
    #     app = application.Application()
    #     self.mine_sweeper = app.start(PATH_TO_GAME)

    def set_up_game(self):
        app = application.Application()
        self.mine_sweeper = app.start(PATH_TO_GAME)
        screen_game = win32gui.FindWindow(None, PATH_TO_GAME.split("\\")[-1])
        win32gui.ShowWindow(screen_game, win32con.SW_MAXIMIZE)

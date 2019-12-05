# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:51:53 2018

@author: initial-h
"""

from __future__ import print_function
from game_board import Board, Game
from mcts_pure import MCTSPlayer as MCTS_pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_tensorlayer import PolicyValueNet
import time
from os import path
import os
from collections import defaultdict

from GUI_menu import Gui_menu

class Human(object):
    """
    human player
    """
    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board,is_selfplay=False,print_probs_value=0):
        # no use params in the func : is_selfplay,print_probs_value
        # just to stay the same with AI's API
        try:
            location = input("Your move: ")
            if isinstance(location, str):  # for python3
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("invalid move")
            move,_ = self.get_action(board)
        return move,None

    def __str__(self):
        return "Human {}".format(self.player)

class Main():

    def __init__(self):
        # def run(start_player=0,is_shown=1):
        self.start_player = 0
        self.is_shown = 1
        menu = Gui_menu()

        # run a gomoku game with AI
        # you can set
        # human vs AI or AI vs AI
        self.n = 5 # Rule 5 목

        if menu.rule == 11 :
            width, height = 11, 11      # 바둑판의 폭과 높이
            model_file = 'model_11_11_5/best_policy.model'
        elif menu.rule == 15 :
            width, height = 15, 15  # 바둑판의 폭과 높이
            model_file = 'model_15_15_5/best_policy.model'

        p = os.getcwd()  # 현재 작업 경로를 얻음
        model_file = path.join(p,model_file)    # 파일 경로 + model file name

        board = Board(width=width, height=height, n_in_row=self.n)   # 게임 판
        game = Game(board)

        mcts_player = MCTS_pure(5,400)

        best_policy = PolicyValueNet(board_width=width,board_height=height,block=19,init_model=model_file,cuda=True)

        # alpha_zero vs alpha_zero

        # best_policy.save_numpy(best_policy.network_all_params)
        # best_policy.load_numpy(best_policy.network_oppo_all_params)
        alpha_zero_player = MCTSPlayer(policy_value_function=best_policy.policy_value_fn_random,
                                       action_fc=best_policy.action_fc_test,
                                       evaluation_fc=best_policy.evaluation_fc2_test,
                                       c_puct=5,
                                       n_playout=400,
                                       is_selfplay=False)

        # alpha_zero_player_oppo = MCTSPlayer(policy_value_function=best_policy.policy_value_fn_random,
        #                                     action_fc=best_policy.action_fc_test_oppo,
        #                                     evaluation_fc=best_policy.evaluation_fc2_test_oppo,
        #                                     c_puct=5,
        #                                     n_playout=400,
        #                                     is_selfplay=False)

        # human player, input your move in the format: 2,3
        # set start_player=0 for human first
        # play in termianl without GUI

        # human = Human()
        # win = game.start_play(human, alpha_zero_player, start_player=start_player, is_shown=is_shown,print_prob=True)
        # return win

        # play in GUI
        game.start_play_with_UI(alpha_zero_player)


if __name__ == '__main__': # 만일 이 파일이 인터프리터에 의해서 실행되는 경우라면, 이라는 의미
                            # 위 if __name__ == '__main__' : 이 있으면, 위 코드는 인터프리터에 의해
                            # 직접 실행될 경우에만 실행하도록 하고 싶은 코드 블럭이 있는 경우에 사용
    main = Main()          # run(start_player=0,is_shown=True)

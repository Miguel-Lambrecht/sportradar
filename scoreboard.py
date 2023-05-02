# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:04:54 2023

@author: ML
"""

from datetime import datetime
import uuid

class OngoingGame:
    '''Class representing an ongoing game'''

    def __init__(self, home_team, away_team, starting_time: datetime=datetime.now()):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        self.starting_time = starting_time

    def update_score(self, new_home_score: int, new_away_score: int) :
        self.home_score = new_home_score
        self.away_score = new_away_score
        
    def total_score(self) -> int:
        '''returns the sum of home and away scores'''
        return self.home_score + self.away_score

    def __repr__(self):
        return str((self.home_team, self.away_team, self.home_score, self.away_score, self.starting_time.strftime("%d/%m, %H:%M")))

class ScoreBoard:
    '''Class representing a scoreboard of OngoingGames'''

    def __init__(self):
        self.__board = {}

    def start_new_game (self, home_team, away_team, starting_time: datetime=datetime.now()) -> str:
        new_game_id=str(uuid.uuid4())
        new_game=OngoingGame(home_team, away_team, starting_time)
        self.__board[new_game_id]=new_game
        return new_game_id

    def finish_game(self, game_id) -> bool:
        if game_id in self.__board:
            del self.__board[game_id]
            return True
        return False
    
    def update_score(self, game_id, home_score, away_score) -> bool:
        if game_id in self.__board:
            self.__board[game_id].update_score(home_score, away_score)
            return True
        return False

    def get_summary(self) -> tuple:
        return []
    
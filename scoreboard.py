# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:04:54 2023

@author: ML
"""
from datetime import datetime
import uuid
import copy

class OngoingGame:
    '''Class representing an ongoing game'''

    def __init__(self, home_team, away_team, starting_time: datetime=datetime.now()):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        if not isinstance(starting_time, datetime):
            raise TypeError("Only datetime argument allowed")
        self.starting_time = starting_time

    def update_score(self, new_home_score: int, new_away_score: int) -> bool:
        '''changes the values of attributes home_score and away_score
        returns True if update is performed, returns False if update is not performed'''
        if not (isinstance(new_home_score, int) and isinstance(new_away_score, int)):
            return False
        self.home_score = new_home_score
        self.away_score = new_away_score
        return True

    def total_score(self) -> int:
        '''returns the sum of home and away scores'''
        return self.home_score + self.away_score

    def __gt__(self, obj):
        '''greater than operator, comparing total score and most recently
        started game if total scores are equal'''
        if self.total_score() == obj.total_score():
            return self.starting_time > obj.starting_time
        return self.total_score() > obj.total_score()

    def __lt__(self, obj):
        '''lower than operator, comparing total score and most recently
        started game if total scores are equal'''
        if self.total_score() == obj.total_score():
            return self.starting_time < obj.starting_time
        return self.total_score() < obj.total_score()

    def __eq__(self, obj):
        '''equal operator, comparing total score and starting time'''
        if isinstance(obj, OngoingGame):
            return ((self.total_score() == obj.total_score()) 
                and (self.starting_time == obj.starting_time))
        return False

    def __repr__(self):
        return str((self.home_team, self.away_team, self.home_score, self.away_score, self.starting_time.strftime("%d/%m, %H:%M")))

class ScoreBoard:
    '''Class representing a scoreboard of OngoingGames'''

    def __init__(self):
        self.__board = {}

    def start_new_game (self, home_team, away_team, starting_time: datetime=datetime.now()) -> str:
        '''creates an OngoingGame, which is added to the score board.
        It returns the unique key value of the new game in the board.
        If no starting_time is passed as argument it will store execution time by default'''
        new_game_id=str(uuid.uuid4())
        new_game=OngoingGame(home_team, away_team, starting_time)
        self.__board[new_game_id]=new_game
        return new_game_id

    def finish_game(self, game_id) -> bool:
        '''removes a game from the score board and returns True.
        If the game is not in the score board, it returns False'''
        if game_id in self.__board:
            del self.__board[game_id]
            return True
        else:
            return False
    
    def update_score(self, game_id, home_score, away_score) -> bool:
        '''updates the score of the game referenced by game_id
        returns True when update is successfull and False if not'''
        if game_id in self.__board:
            return self.__board[game_id].update_score(home_score, away_score)            
        else:
            return False

    def get_summary(self) -> tuple:
        '''returns the scoreboard content as a sorted tuple of OngoingGame instances.
        The OngoingGame instances of the summary are copies of the ongoing games 
        at the time of the get_summary call. The returned summary is a snapshot that won't
        be modified even when the scores of the various games changes or games
        are finished'''
        games_immutable_copy = [copy.copy(game) for game in self.__board.values()]
        return tuple(sorted(games_immutable_copy,reverse=True))
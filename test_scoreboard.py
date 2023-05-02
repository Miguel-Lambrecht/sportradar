# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:41:54 2023

@author: ML
"""
import unittest
from datetime import datetime, timedelta
from scoreboard import ScoreBoard, OngoingGame

class ScoreBoardTestCase(unittest.TestCase):
    
    def test_ScoreBoard(self):
        
        #games started in this specific order
        started_games=(("Mexico", "Canada", 0, 5),
                       ("Spain","Brazil", 10, 2),
                       ("Germany","France", 2, 2),
                       ("Uruguay", "Italy",6 ,6),
                       ("Argentina","Australia", 6, 6))
        
        #expected summary ranking of the same games
        expected_summary=(started_games[3],
                          started_games[1],
                          started_games[0],
                          started_games[4],
                          started_games[2])
        
        #create empty scoreboard               
        board = ScoreBoard()
        
        #set times and time shift between games
        initial_time = datetime.now()
        time_delta = timedelta(minutes=10)
        
        #start the games one after the other with a time delta and update scores
        starting_time=initial_time
        for game in started_games:
            game_id=board.start_new_game(game[0], game[1], starting_time)
            board.update_score(game_id, game[2], game[3])
            starting_time+=time_delta
        
        #get the score board summary
        summary=board.get_summary()
        
        #test the amount of items in the summary
        self.assertEqual(len(expected_summary), len(summary))
        
        #test the content of the summary
        for i in range(len(summary)):
            expected_home_team=expected_summary[i][0]
            expected_away_team=expected_summary[i][1]
            expected_home_score=expected_summary[i][2]
            expected_away_score=expected_summary[i][3]
            
            self.assertEqual(expected_home_team, summary[i].home_team)
            self.assertEqual(expected_away_team, summary[i].away_team)
            self.assertEqual(expected_home_score, summary[i].home_score)
            self.assertEqual(expected_away_score, summary[i].away_score)
            
class OngoingGameTestCase(unittest.TestCase):
    
    def test_OngoingGame(self):
        
        game=OngoingGame("France", "Mexico")
        self.assertEqual("France", game.home_team)
        self.assertEqual("Mexico", game.away_team)
        self.assertEqual(0, game.home_score)
        self.assertEqual(0, game.away_score)
        self.assertEqual(True, isinstance(game.starting_time, datetime))
        
        starting=datetime.now()
        game=OngoingGame("France", "Mexico",starting)
        self.assertEqual(starting, game.starting_time)
        
              
    def test_update_score(self):
        #method update_score modifies scores
        home="France"
        away="Mexico"
        starting=datetime.now()
        game=OngoingGame(home, away, starting)
        game.update_score(2,10)
        self.assertEqual(2, game.home_score)
        self.assertEqual(10, game.away_score)
        self.assertEqual(home, game.home_team)
        self.assertEqual(away, game.away_team)
        self.assertEqual(starting, game.starting_time)
        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:41:54 2023

@author: ML
"""
import unittest
from datetime import datetime, timedelta
from scoreboard import ScoreBoard, OngoingGame

class OngoingGameTestCase(unittest.TestCase):
    
    def test_OngoingGame(self):
        
        #basic tests
        game=OngoingGame("France", "Mexico")
        self.assertEqual("France", game.home_team)
        self.assertEqual("Mexico", game.away_team)
        self.assertEqual(0, game.home_score)
        self.assertEqual(0, game.away_score)
        self.assertEqual(True, isinstance(game.starting_time, datetime))
        
        #argument starting_time
        starting=datetime.now()
        game=OngoingGame("France", "Mexico",starting)
        self.assertEqual(starting, game.starting_time)
        
        #argument starting_time datetime only
        with self.assertRaises(TypeError):
            game=OngoingGame("France", "Mexico", 10)
                    
    def test_update_score(self):
        home="France"
        away="Mexico"
        starting_time=datetime.now()
        game=OngoingGame(home, away, starting_time)
        game.update_score(2,10)
        self.assertEqual(2, game.home_score)
        self.assertEqual(10, game.away_score)
        self.assertEqual(home, game.home_team)
        self.assertEqual(away, game.away_team)
        self.assertEqual(starting_time, game.starting_time)
        
    def test_total_score(self):
        game=OngoingGame("A","B")
        self.assertEqual(0, game.total_score())
        game.update_score(10,0)
        self.assertEqual(10, game.total_score())
        game.update_score(10,2)
        self.assertEqual(12, game.total_score())
        
    def test___gt__(self):
        starting_time=datetime.now()
        time_delta = timedelta(minutes=10)
        
        #same starting time
        game1=OngoingGame("A", "B", starting_time)
        game2=OngoingGame("C", "D", starting_time)
        game1.update_score(5,2)
        
        #same total score and same starting time
        game2.update_score(5,2)
        self.assertEqual(False, game2>game1)
        self.assertEqual(False, game1>game2)
        
        #different total score and same starting time
        game2.update_score(4,2)
        self.assertEqual(False, game2>game1)
        self.assertEqual(True, game1>game2)
        
        #different starting time
        game1=OngoingGame("A", "B", starting_time)
        game2=OngoingGame("C", "D", starting_time+time_delta)
        game1.update_score(5,2)
        
        #same total score and different starting time
        game2.update_score(5,2)
        self.assertEqual(True, game2>game1)
        self.assertEqual(False, game1>game2)
        
        #different total score and different starting time
        game2.update_score(4,2)
        self.assertEqual(False, game2>game1)
        self.assertEqual(True, game1>game2)
        
class ScoreBoardTestCase(unittest.TestCase):
      
    def test_update_score(self):
        board = ScoreBoard()
        
        #start 1 game
        game1 = board.start_new_game("A","B")
                
        #update score
        self.assertEqual(False, board.update_score(game1, "two", 1)) #int arguments required
        self.assertEqual(True, board.update_score(game1, 2, 0))
            
    def test_finish_game(self):
        board = ScoreBoard()
        
        #start 2 games
        game1 = board.start_new_game("A","B")
        game2 = board.start_new_game("C","D")
        
        #finish game1
        self.assertEqual(True, board.finish_game(game1))
        
        #check that game1 is removed
        self.assertEqual(False, board.update_score(game1, 1, 1)) #unable to update a finished game
        self.assertEqual(False, board.finish_game(game1)) #unable to finish already finished game
        
        #and game2 still in the scoreboard
        self.assertEqual(True, board.update_score(game2, 1, 1))
        self.assertEqual(True, board.finish_game(game2))
       
    def test_get_summary(self):
        #games started in this specific order
        started_games=(("Mexico", "Canada", 0, 5),
                       ("Spain","Brazil", 10, 2),
                       ("Germany","France", 2, 2),
                       ("Uruguay", "Italy",6 ,6),
                       ("Argentina","Australia", 3, 1))
        
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
            
                    

        
        
        
        
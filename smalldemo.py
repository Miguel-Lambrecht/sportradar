# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:06:20 2023

@author: ML

Description: the only purpose is to demo the utilization of the ScoreBoard library.
Displaying a representation of the score board summary after various score board events,
like start new game, update score and finish game
"""
from datetime import datetime, timedelta
from scoreboard import ScoreBoard, OngoingGame

def display_scoreboard(s: ScoreBoard):
    '''this function only displays the summary of a scoreboard'''
    def display_game(g: OngoingGame):
        team_size=15
        score_size=3
        date_size=10
        string_game = (g.home_team.rjust(team_size) + 
                       str(g.home_score).rjust(score_size) +
                       " : " + 
                       str(g.away_score).ljust(score_size) + 
                       g.away_team.ljust(team_size) +
                       g.starting_time.strftime("%d/%m, %H:%M").rjust(date_size) +
                       '\n')
        print(string_game)
        
    for game in s.get_summary():
        display_game(game)

#creating the Score Board        
demo_scoreboard=ScoreBoard()
initial_time = datetime.now()
time_delta = timedelta(minutes=10)

display_scoreboard(demo_scoreboard)

print("3 games start at the same time, the scoreboard:")
starting_time=initial_time
Mex_Can=demo_scoreboard.start_new_game("Mexico", "Canada", starting_time)
Spa_Bra=demo_scoreboard.start_new_game("Spain", "Brazil", starting_time)
Ger_Sen=demo_scoreboard.start_new_game("Germany", "Senegal", starting_time)
display_scoreboard(demo_scoreboard)

print("Germany scores! the scoreboard:")
demo_scoreboard.update_score(Ger_Sen,1,0)
display_scoreboard(demo_scoreboard)     

print("2 games start at the same time, 10 minutes after the first 3 games, the scoreboard:")
starting_time+=time_delta
Fra_Arg=demo_scoreboard.start_new_game("France", "Argentina", starting_time)
Cro_Mor=demo_scoreboard.start_new_game("Croatia", "Morocco", starting_time)        
display_scoreboard(demo_scoreboard)

print("Argentina scores! the scoreboard:")
demo_scoreboard.update_score(Fra_Arg,0,1)
display_scoreboard(demo_scoreboard)

print("Mexico and Canada score! the scoreboard:")
demo_scoreboard.update_score(Mex_Can,1,1)
display_scoreboard(demo_scoreboard)

print("France and Brazil score! the scoreboard:")
demo_scoreboard.update_score(Fra_Arg,1,1)
demo_scoreboard.update_score(Spa_Bra,0,1)
display_scoreboard(demo_scoreboard)        

print("Spain scores twice! the scoreboard:")
demo_scoreboard.update_score(Spa_Bra,2,1)
display_scoreboard(demo_scoreboard)        

print("Mexico vs Canada is over, the scoreboard:")
demo_scoreboard.finish_game(Mex_Can)
display_scoreboard(demo_scoreboard) 

print("End of the demo, just scroll up your screen to observe the changes in the scoreboard based on events.")
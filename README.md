
# Live Football World Cup Score Board Library

The intent is to provide means for handling a live scoreboard that shows all the ongoing matches and their scores.
The scoreboard supports the following operations:
1. Start a new game, assuming initial score 0 – 0 and adding it to the scoreboard.
This should capture following parameters:
a. Home team
b. Away team

2. Update score. This should receive a pair of absolute scores: home team score and away
team score.

3. Finish game currently in progress. This removes a match from the scoreboard.

4. Get a summary of games in progress ordered by their total score. The games with the same total score will be returned ordered by the most recently started match in the scoreboard.


## Demo


The get_summary method works as follow. If the following games are started in the specified order and their scores respectively updated:

a. Mexico 0 - Canada 5

b. Spain 10 - Brazil 2

c. Germany 2 - France 2

d. Uruguay 6 - Italy 6

e. Argentina 3 - Australia 1



The summary should be as follows:
1. Uruguay 6 - Italy 6
2. Spain 10 - Brazil 2
3. Mexico 0 - Canada 5
4. Argentina 3 - Australia 1
5. Germany 2 - France 2


## Features

- 2 classes are implemented:
    - OngoingGame: implementing individual game
    - ScoreBoard: implementing a collection of OngoingGame

The OngoingGame instances contained in the ScoreBoard can be handled only via the ScoreBoard instance.

The ScoreBoard content can be obtained only via the get_summary method which returns a tuple of OngoingGame instances ordered by total score and starting time if total scores are equal.

The OngoingGame instances contained in the tuple returned by the get_summary method are independent from the OngoingGame instances contained in the ScoreBoard collection (they are copies).


## Usage/Examples

The smalldemo.py file provides an example of utilization of the library.


## Running Tests

Unit tests are in the test_scoreboard.py file and are dependent on unittest library.
Tests can be run locally with the instruction:

  python -m unittest



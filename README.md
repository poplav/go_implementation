A minimal framework for writing computer go players and simulating play against each other.
* Players can be implemented via defining a `get_move` function accepting the board/state at [/players](go_implementation/players)
* The base simulator for playing games taking in two players and returning the state history/stats of the game is at [/game_simulators](go_implementation/game_simulators)
* Examples and benchmarks of different players against each other can be found in the notebook section at [notebooks](/resources/notebooks)

This repo builds on top of Brian Lee's [go_implementations](https://github.com/brilee/go_implementation)
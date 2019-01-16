from go_implementation.base_implementation.go_sets import Position, WHITE, BLACK
from go_implementation.players.random_player import RandomPlayer
import time


class GameSimulator:

    def __init__(self):
        self.position = Position.initial_state()

    def play_game(self, player_one, player_two):
        state_history = []
        toggle_turn = True
        consecutive_passes = 0
        player_move_time = {BLACK: 0, WHITE: 0}
        while consecutive_passes < 2:
            current_player = player_one if toggle_turn else player_two
            move_time_start = time.time()
            move = current_player.get_move(self.position.get_board())
            move_time = time.time() - move_time_start
            player_move_time[current_player.color] += move_time
            if move:
                self.position = self.position.play_move(move[1], move[0])
                player_one.ko = self.position.ko
                player_two.ko = self.position.ko
                consecutive_passes = 0
            else:
                consecutive_passes += 1
            toggle_turn = not toggle_turn
            current_state = (
                str(self.position),
                self.position.score(),
                player_move_time.copy()
            )
            state_history.append(current_state)
            #print(self.position)
            #print("============================ , " + str(self.position.score()))
        return state_history


if __name__ == '__main__':
    game_sim = GameSimulator()
    player_one = RandomPlayer(BLACK)
    player_two = RandomPlayer(WHITE)
    start = time.time()
    game_state_history = game_sim.play_game(player_one, player_two)
    end = time.time()
    print("game finished, num moves = ", len(game_state_history))
    print("game time is ", (end-start))
    print("player move time is ", game_state_history[-1])

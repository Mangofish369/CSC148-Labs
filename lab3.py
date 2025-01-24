"""CSC148 Lab 3: Inheritance

=== CSC148 Winter 2025 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.
"""
from __future__ import annotations
import random

from python_ta.contracts import check_contracts


################################################################################
# Below is the implementation of NumberGame.
#
# You do not have to modify this class, but you should read through it and
# understand how it uses the Player class (and its subclasses) that you'll
# be implementing.
#
# As you read through, make note of any methods or attributes a Player will
# need.
################################################################################
@check_contracts
class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.

    The game can have multiple rounds.

    Attributes:
    - goal:
        The amount to reach in order to win the game.
    - min_step:
        The minimum legal move.
    - max_step:
        The maximum legal move.
    - current:
        The current value of the game count.
    - players:
        The two players.
    - turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    Representation Invariants:
    - self.turn >= 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """
    goal: int
    min_step: int
    max_step: int
    current: int
    players: tuple[Player, Player]
    turn: int

    def __init__(self, goal: int, min_step: int, max_step: int,
                 players: tuple[Player, Player]) -> None:
        """Initialize this NumberGame.

        Preconditions:
        - 0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        loser = self.whose_turn(self.turn)
        winner = self.whose_turn(self.turn - 1)
        winner.record_win()
        loser.record_loss()
        return winner.name

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        self.current += amount

        # We set a hard limit on self.current
        # (This is a strange corner case: don't worry about it!)
        if self.current > self.goal:
            self.current = self.goal

        self.turn += 1

        print(f'{next_player.name} moves {amount}.')
        print(f'Total is now {self.current}.')


################################################################################
# Implement your Player class and it subclasses below!
################################################################################

class Player:
    """
    A general category for players. With three levels of difficulty.
    Random, User, Strategic.

    Attributes:
        - name: The player's name
        - wins: The number of wins the player has this session
        - losses:   The number of losses the player has this session
    """
    name: str
    wins: int
    losses: int

    def __init__(self, name: str) -> None:
        self.wins = 0
        self.losses = 0
        self.name = name

    def move(self, cur_count: int, min_step: int, max_step: int, goal: int) -> int:
        """
        Prints the minimum and maximum step, returns the move chosen
        """
        raise NotImplementedError

    def record_win(self) -> None:
        """
        Add one win
        """
        self.wins += 1

    def record_loss(self) -> None:
        """
        Add one loss
        """
        self.losses += 1


class UserPlayer(Player):
    """
    The user player lets the user choose their move on their turn
    """
    def move(self, cur_count: int, min_step: int, max_step: int, goal: int) -> int:
        """
        Prints the current count, and possible choices for move.

        Preconditions:
        user input is an integer from min_step to max_step
        """
        user_num = '0'
        while user_num.isdigit() == False and (int(user_num) > min_step or int(user_num) > max_step):
            user_num = input(f'Enter a number from {min_step} to {max_step}: ')
        return int(user_num)


class RandomPlayer(Player):
    """
    The random player picks a random valid move on their turn
    """
    def move(self, cur_count: int, min_step: int, max_step: int, goal: int) -> int:
        """
        Picks a random valid number as their move for the turn
        """
        num = random.randint(min_step, max_step)
        return num
class StrategicPlayer(Player):
    def move(self, cur_count: int, min_step: int, max_step: int, goal: int) -> int:
        """
        Picks a more optimized valid number as their move for the turn
        """
        goal = 21
        while goal-cur_count >= max_step:
            goal-=4
        num = goal-cur_count
        return num

@check_contracts
def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.

    If the inputted name starts with an "s", make a StrategicPlayer.
    If the inputted name starts with a "u", make a UserPlayer.
    Otherwise, make a RandomPlayer.
    """
    name = input(f'Enter a name for {generic_name}: ')
    if 'u' == name[0]:
        player = UserPlayer(name)
    else:
        player = RandomPlayer(name)
    return player


################################################################################
# The main game program
################################################################################

def main() -> None:
    """Play multiple rounds of a NumberGame based on user input settings.
    """
    goal = int(input('Enter goal amount: '))
    minimum = int(input('Enter minimum move: '))
    maximum = int(input('Enter maximum move: '))
    p1 = make_player('p1')
    p2 = make_player('p2')
    while True:
        g = NumberGame(goal, minimum, maximum, (p1, p2))
        winner = g.play()
        print(f'And {winner} is the winner!!!')
        print(p1)
        print(p2)
        again = input('Again? (y/n) ')
        if again != 'y':
            return


if __name__ == '__main__':
    # Uncomment the following line to run the number game.
    # main()

    # Uncomment to check your work with python_ta!
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['random'],
        'allowed-io': [
            'main',
            'make_player',
            'UserPlayer.move',
            'NumberGame.play_one_turn'
        ],
        'max-line-length': 100
    })

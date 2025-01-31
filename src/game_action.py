from enum import IntEnum

class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZZARD = 3
    SPOCK = 4

    @classmethod
    def minus(cls, *actions_excluded):
        return [action for action in GameAction if action not in actions_excluded]
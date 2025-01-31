from src.game_action import GameAction

VICTORIES = {
    GameAction.ROCK: (GameAction.PAPER, GameAction.SPOCK),
    GameAction.PAPER: (GameAction.SCISSORS, GameAction.LIZZARD),
    GameAction.SCISSORS: (GameAction.ROCK, GameAction.SPOCK),
    GameAction.LIZZARD: (GameAction.SCISSORS, GameAction.ROCK),
    GameAction.SPOCK: (GameAction.LIZZARD, GameAction.PAPER)
}
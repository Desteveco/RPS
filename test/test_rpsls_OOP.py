import pytest
from src.rpsls_OOP import Game
from src.game_action import GameAction
from src.game_result import GameResult


@pytest.fixture
def game():
    '''
    Setup del objeto game
    '''
    setup_game = Game()
    return setup_game


@pytest.mark.draw
def test_draw(game):

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.LIZZARD)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SCISSORS)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)


@pytest.mark.spock
def test_spock_loses(game):
    '''
    Spock pierde con lizzard y paper 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SPOCK)

    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SPOCK)


@pytest.mark.spock
def test_spock_wins(game):
    '''
    Spock gana a Rock y Scissors 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SPOCK)


@pytest.mark.lizzard
def test_lizzard_loses(game):
    '''
    lizzard pierde con Rock y Scissors 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.LIZZARD)

    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.LIZZARD)


@pytest.mark.lizzard
def test_lizzard_wins(game):
    '''
    lizzard gana a Spock y paper 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.LIZZARD)

    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.LIZZARD)


@pytest.mark.rock
def test_rock_loses(game):
    '''
    Rock pierde con Spock y paper 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.ROCK)

    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)


@pytest.mark.rock
def test_rock_wins(game):
    '''
    Rock gana a Scissors y lizzard 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)

    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.ROCK)


@pytest.mark.paper
def test_paper_loses(game):
    '''
    paper pierde con Scissors y lizzard 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)

    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.PAPER)


@pytest.mark.paper
def test_paper_wins(game):
    '''
    paper gana a Rock y Spock 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.PAPER)


@pytest.mark.scissors
def test_scissors_loses(game):
    '''
    Scissors pierde con Spock y Rock 
    '''
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SCISSORS)

    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.scissors
def test_scissors_wins(game):
    '''
    Scissors gana a lizzard y paper 
    '''
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SCISSORS)

    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)


@pytest.mark.actions
def test_minus_action():
    '''
    GameActions EnumType behaviour
    '''
    assert 1 == len(GameAction.minus(
        GameAction.Scissors,
        GameAction.Lizard,
        GameAction.Paper,
        GameAction.Rock))

    assert 4 == len(GameAction.minus(GameAction.Lizard))

    assert GameAction.Lizard not in GameAction.minus(GameAction.Lizard)

    assert GameAction.Lizard in GameAction.minus(GameAction.Spock, GameAction.Rock)
import pytest
from src.rpsls_OOP import assess_game
from src.game_action import GameAction
from src.game_result import GameResult

@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameResult.Tie == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.SCISSORS, 
        computer_action=GameAction.SCISSORS)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)
    
    assert GameResult.Tie == assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.LIZZARD)
    
    assert GameResult.Tie == assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SPOCK)

import pytest
from enum import IntEnum

# Definiciones de las clases GameAction y GameResult
class GameAction(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZZARD = 3
    SPOCK = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


# Función assess_game (simulada para los tests)
def assess_game(user_action, computer_action):
    if user_action == computer_action:
        return GameResult.Tie

    victories = {
        GameAction.ROCK: [GameAction.SCISSORS, GameAction.LIZZARD],
        GameAction.PAPER: [GameAction.ROCK, GameAction.SPOCK],
        GameAction.SCISSORS: [GameAction.PAPER, GameAction.LIZZARD],
        GameAction.LIZZARD: [GameAction.PAPER, GameAction.SPOCK],
        GameAction.SPOCK: [GameAction.ROCK, GameAction.SCISSORS]
    }

    if computer_action in victories[user_action]:
        return GameResult.Victory
    else:
        return GameResult.Defeat


# Tests para Rock
@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper (usuario elige Paper, computadora elige Rock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)


@pytest.mark.rock
def test_rock_loses2():
    '''
    Rock pierde con Spock (usuario elige Spock, computadora elige Rock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.ROCK)


@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors (usuario elige Rock, computadora elige Scissors)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.rock
def test_rock_wins2():
    '''
    Rock gana a Lizard (usuario elige Rock, computadora elige Lizard)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.LIZZARD)


# Tests para Paper
@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors (usuario elige Scissors, computadora elige Paper)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)


@pytest.mark.paper
def test_paper_loses2():
    '''
    Paper pierde con Lizard (usuario elige Lizard, computadora elige Paper)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.PAPER)


@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock (usuario elige Paper, computadora elige Rock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)


@pytest.mark.paper
def test_paper_wins2():
    '''
    Paper gana a Spock (usuario elige Paper, computadora elige Spock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SPOCK)


# Tests para Scissors
@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock (usuario elige Rock, computadora elige Scissors)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.scissors
def test_scissors_loses2():
    '''
    Scissors pierde con Spock (usuario elige Spock, computadora elige Scissors)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper (usuario elige Scissors, computadora elige Paper)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)


@pytest.mark.scissors
def test_scissors_wins2():
    '''
    Scissors gana a Lizard (usuario elige Scissors, computadora elige Lizard)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.LIZZARD)


# Tests para Lizard
@pytest.mark.lizzard
def test_lizard_loses():
    '''
    Lizard pierde con Rock (usuario elige Rock, computadora elige Lizard)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.LIZZARD)


@pytest.mark.lizzard
def test_lizard_loses2():
    '''
    Lizard pierde con Scissors (usuario elige Scissors, computadora elige Lizard)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.LIZZARD)


@pytest.mark.lizzard
def test_lizard_wins():
    '''
    Lizard gana a Paper (usuario elige Lizard, computadora elige Paper)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.PAPER)


@pytest.mark.lizzard
def test_lizard_wins2():
    '''
    Lizard gana a Spock (usuario elige Lizard, computadora elige Spock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SPOCK)


# Tests para Spock
@pytest.mark.spock
def test_spock_loses():
    '''
    Spock pierde con Lizard (usuario elige Lizard, computadora elige Spock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SPOCK)


@pytest.mark.spock
def test_spock_loses2():
    '''
    Spock pierde con Paper (usuario elige Paper, computadora elige Spock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SPOCK)


@pytest.mark.spock
def test_spock_wins():
    '''
    Spock gana a Rock (usuario elige Spock, computadora elige Rock)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.ROCK)


@pytest.mark.spock
def test_spock_wins2():
    '''
    Spock gana a Scissors (usuario elige Spock, computadora elige Scissors)
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SCISSORS)
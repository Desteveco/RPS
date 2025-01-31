import pytest
from src.rps_basic import GameResult, GameAction, assess_game

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

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)

@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)

@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)

@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)

@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper 
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)
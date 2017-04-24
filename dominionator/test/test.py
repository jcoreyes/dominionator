from game.game import Game
from player.player import HumanPlayer
from cards.card_names import BASE_SET

if __name__ == '__main__':
    players = [HumanPlayer('Player 1'), HumanPlayer('Player2')]
    game = Game(BASE_SET, players)
    game.play()


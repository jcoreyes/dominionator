from queue import deque
from cards.cards import Copper, Estate
from cards.card_names import ACTION_TYPE
from random import shuffle

END_ACTION = -1
END_TURN = -1

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        for i in range(7):
            self.deck.append(Copper())
        for i in range(3):
            self.deck.append(Estate())

        self.discard = []
        self.hand = []
        self.in_play = []
        self.hand_size = 5
        self.actions = 1
        self.buys = 1
        self.buying_power = 0

        shuffle(self.deck)
        self.draw_hand(5)

    def draw_hand(self, draw):
        self.hand = []
        for i in range(draw):
            if len(self.deck) > 0:
                self.hand.append(self.deck.pop())
            else:
                self.deck = self.discard
                shuffle(self.deck)

    def add_buying_power(self, value):
        self.buying_power += value

    def add_actions(self, value):
        self.actions += value

    def add_buys(self, value):
        self.buys += value

    def hand_str(self):
        return ' '.join([str(x) for x in self.hand])

    def cleanup_phase(self, game):
        self.discard += self.in_play
        self.discard += self.hand
        self.in_play = []
        self.draw_hand(5)

        self.actions = 1
        self.buys = 1
        self.buying_power = 0

class HumanPlayer(Player):
    def play_turn(self, game):
        print(self.name)
        self.action_phase(game)
        self.buy_phase(game)
        self.cleanup_phase(game)


    def request_action(self):
        action_idx = int(input('Input action no from hand %s\n' %self.hand_str()))
        if action_idx is not END_ACTION:
            return self.hand.pop(action_idx)
        else:
            return action_idx

    def play_action(self, game, card):
        card.play(self, game)
        print(self.hand_str())

    def action_phase(self, game):
        no_actions = True
        for card in self.hand:
            if ACTION_TYPE not in card.kind:
                no_actions = False
                break
        if no_actions:
            return

        while self.actions > 0:
            action_card = self.request_action()
            if action_card is not END_ACTION:
                self.actions -= 1
                self.in_play.append(action_card)
                self.play_action(game, action_card)
            else:
                break

    def buy_phase(self, game):
        while self.buys > 0:
            card = game.request_buy()
            if card is not None:
                self.discard.append(card)
                self.buys -= 1
            else:
                break




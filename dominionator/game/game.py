import numpy as np
from cards.card_names import VICTORY_CARDS, TREASURE_CARDS
from cards.cards import make_card
from player.player import END_TURN

class Game:
    def __init__(self, kingdom_cards, players):
        """

        :param cards: list of strings
        :param players: list of players
        """
        self.kingdom_cards = kingdom_cards
        self.victory_cards = VICTORY_CARDS
        self.treasure_cards = TREASURE_CARDS
        self.cards = self.kingdom_cards + self.victory_cards + self.treasure_cards

        self.players = players

        self.card_idx = {self.cards[idx]:idx for idx in range(len(self.cards))}
        self.idx_card = {idx:card for card,idx in self.card_idx.items()}
        self.num_players = len(players)

        if self.num_players <= 4:
            self.supply_limit = 3
            if self.num_players == 2:
                self.vic_supply = 8
            else:
                self.vic_supply = 12
        else:
            self.supply_limit = 4
            self.vic_supply = 16

        self.card_counts = np.zeros(len(self.cards))
        for card, idx in self.card_idx.items():
            if card in self.victory_cards:
                self.card_counts[idx] = self.vic_supply
            elif card in self.treasure_cards:
                self.card_counts[idx] = 20
            else:
                self.card_counts[idx] = 10

        self.turn_order = np.random.permutation(range(self.num_players))

    def play(self):
        game_over = False
        while True:
            for player_idx in self.turn_order:
                self.players[player_idx].play_turn(self)
                if self.is_game_over():
                    game_over = True
                    break
            if game_over:
                break
        self.count_victory()

    def request_buy(self):
        buy_idx = int(input('Buy Card idx %s\n' %' '.join([str(x) for x in self.cards])))
        if buy_idx == END_TURN:
            return None
        else:
            self.card_counts[buy_idx] -= 1
            card_name = self.idx_card[buy_idx]
            return make_card(card_name)

    def is_game_over(self):
        if (self.card_counts == 0).sum() == self.supply_limit:
            return True
        if self.card_counts[self.card_idx[self.victory_cards[-1]]] == 0:
            return True
        return False


    def count_victory(self):
        pass
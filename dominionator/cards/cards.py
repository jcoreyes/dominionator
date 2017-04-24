
from cards.card_names import TREASURE_TYPE, VICTORY_TYPE, ACTION_TYPE

def make_card(name):
    return globals()[name]

class Card:
    def __init__(self):
        self.name = self.__class__.__name__.lower()
        self.cost = 0
        self.kind = None

    def __str__(self):
        return self.name

    def play(self, player, game):
        raise NotImplemented

    @property
    def kind(self):
        return self.kind

class TreasureCard(Card):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.kind = set(TREASURE_TYPE)

    def play(self, player, game):
        player.add_buying_power(self.value)



class ActionCard(Card):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.kind = set(ACTION_TYPE)


class Copper(TreasureCard):
    def __init__(self):
        super().__init__()
        self.cost = 0
        self.value = 1

class Silver(TreasureCard):
    def __init__(self):
        super().__init__()
        self.cost = 3
        self.value = 2

class Gold(TreasureCard):
    def __init__(self):
        super().__init__()
        self.cost = 6
        self.value = 3

class VictoryCard(Card):
    def __init__(self):
        super().__init__()
        self.kind = set(VICTORY_TYPE)

class Estate(VictoryCard):
    def __init__(self):
        super().__init__()
        self.cost = 2
        self.points = 1

class Duchy(VictoryCard):
    def __init__(self):
        super().__init__()
        self.cost = 5
        self.points = 3

class Province(VictoryCard):
    def __init__(self):
        super().__init__()
        self.cost = 8
        self.points = 6

class Smithy(ActionCard):
    def play(self, player, game):
        player.draw_hand(3)

class Village(ActionCard):
    def play(self, player, game):
        player.draw(1)
        player.add_actions(2)

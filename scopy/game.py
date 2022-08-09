from dataclasses import dataclass
import random

SUITS = ("clubs", "spades", "hearts", "diamonds")
FACES = ("A", "2", "3", "4", "5", "6", "7", "J", "Q", "K")
VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
PVALUES = (16, 12, 13, 14, 15, 18, 21, 10, 10, 10)


@dataclass(frozen=True)
class Card:
    suit: str
    face: str
    value: int
    pvalue: int


class Deck:
    SUITS = ("clubs", "spades", "hearts", "diamonds")
    FACES = ("A", "2", "3", "4", "5", "6", "7", "J", "Q", "K")
    VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    PVALUES = (16, 12, 13, 14, 15, 18, 21, 10, 10, 10)

    def __init__(self) -> None:
        self.cards = [
            Card(suit, *args)
            for suit in SUITS
            for args in zip(FACES, VALUES, PVALUES)
        ]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def get_top_card(self) -> None:
        return self.cards.pop()


class Player:
    def __init__(self) -> None:
        self.hand = []

    def draw(self, card: Card) -> None:
        if len(self.hand) >= 3:
            raise ScoPyHandFullException("Cannot draw more than 3 cards!")
        self.hand.append(card)


class Game:
    def __init__(
        self, player1: Player, player2: Player, deck: Deck = Deck()
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

        self.pot = []
        self.is_started = False

    def setup(self) -> None:
        if not self.is_started:
            self.deck.shuffle()
            for _ in range(3):
                self.player2.draw(self.deck.get_top_card())
                self.pot.append(self.deck.get_top_card())
                self.player1.draw(self.deck.get_top_card())
            self.pot.append(self.deck.get_top_card())


class ScoPyHandFullException(Exception):
    pass

from typing import List, Set, Tuple
from dataclasses import dataclass, field
import random


SUITS = ("clubs", "spades", "hearts", "diamonds")
FACES = ("A", "2", "3", "4", "5", "6", "7", "J", "Q", "K")
VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
PVALUES = (16, 12, 13, 14, 15, 18, 21, 10, 10, 10)


@dataclass(frozen=True)
class Card:
    suit: str
    face: str
    value: int = field(init=False)
    pvalue: int = field(init=False)

    def __post_init__(self):
        val_mapping = {k: v for k, v in zip(FACES, VALUES)}
        pval_mapping = {k: v for k, v in zip(FACES, PVALUES)}
        self.value = val_mapping[self.face]
        self.pvalue = pval_mapping[self.face]


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(suit, face) for suit in SUITS for face in FACES]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def get_top_card(self) -> None:
        return self.cards.pop()


class Player:
    def __init__(self, hand: List[Card] = None) -> None:
        self.hand = hand or []
        self.playable_hand = []

    def draw(self, card: Card) -> None:
        if len(self.hand) >= 3:
            raise ScoPyHandFullException("Cannot draw more than 3 cards!")
        self.hand.append(card)

    def filter_playable_hand(self, possible_values: Set[int]):
        self.playable_hand = [
            card for card in self.hand if card.value in possible_values
        ]


class Table:
    def __init__(self, cards: Set[Card]) -> None:
        self.cards = cards

    def get_possible_values() -> Set[int]:
        pass

    def get_possible_moves() -> Tuple[int, List[int]]:
        pass


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

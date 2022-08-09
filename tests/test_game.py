import pytest
from scopy.game import Card, Deck


@pytest.fixture
def deck():
    return Deck()


def test_deck_full(deck):
    assert len(set(deck.cards)) == 40


def test_deck_shuffle(deck):
    deck.shuffle()
    print(deck.cards)
    assert deck.cards[0] != Card("clubs", "A", 1, 16)

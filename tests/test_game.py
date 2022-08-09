import pytest
from scopy.game import Card, Deck, Player, ScoPyHandFullException


@pytest.fixture
def deck():
    return Deck()

@pytest.fixture
def player():
    return Player()


def test_deck_full(deck):
    assert len(set(deck.cards)) == 40


def test_deck_shuffle(deck):
    deck.shuffle()
    print(deck.cards)
    assert deck.cards[0] != Card("clubs", "A", 1, 16)


def test_deck_get_top_card(deck):
    assert deck.get_top_card() == Card("diamonds", "K", 10, 10)


def test_player_draw(player):
    player.draw(Card("clubs", "A", 1, 16))
    assert len(player.hand) == 1


def test_player_overdraw(player):
    player.draw(Card("clubs", "A", 1, 16))
    player.draw(Card("spades", "A", 1, 16))
    player.draw(Card("hearts", "A", 1, 16))
    with pytest.raises(ScoPyHandFullException):
        player.draw(Card("diamonds", "A", 1, 16))
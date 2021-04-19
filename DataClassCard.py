from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


@dataclass
class Deck:
    # cards: List[PlayingCard]

    def make_french_deck():
        return [PlayingCard(s, r) for s in SUITS for r in RANKS]

    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{__class__.__name__}({cards})'


RANKS = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
SUITS = '\u2660 \u2665 \u2663 \u2660'.split()

queen_of_hearts = PlayingCard('Q', 'hearts')
ace_of_spades = PlayingCard('A', 'spades')
two_cards_deck = Deck([queen_of_hearts, ace_of_spades])

french_deck = Deck.make_french_deck()
# print(str(queen_of_hearts))
card = PlayingCard('Q', '\u2665')
# print(two_cards_deck)
# print(french_deck)
print(Deck())
# print(card)

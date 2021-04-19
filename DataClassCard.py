from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

    def make_french_deck():
        return [PlayingCard(r, s) for s in SUITS for r in RANKS]

RANKS = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
SUITS = '\u2660 \u2665 \u2663 \u2660'.split() 

queen_of_hearts = PlayingCard('Q', 'hearts')
ace_of_spades = PlayingCard('A', 'spades')
two_cards_deck = Deck([queen_of_hearts, ace_of_spades])

french_deck = Deck.make_french_deck()
#print(two_cards_deck)
print(french_deck)
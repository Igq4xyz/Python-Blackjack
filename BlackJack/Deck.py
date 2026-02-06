from dataclasses import dataclass
from Card import Card
import random

@dataclass
class Deck:
    cards: list[Card]

    def add_card (self, card: Card):
        if card is not None:
            self.cards.append(card)

        
    def swap_cards_in_deck(self, a: int, b: int):
        aux = self.cards[a]
        self.cards[a]=self.cards[b]
        self.cards[b]=aux
# primero
    def init_deck(self):
        for value in range(1,14):
            self.add_card(Card(value, "Hearts", "Red"))
            self.add_card(Card(value, "Diamonds", "Red"))
            self.add_card(Card(value, "Picas", "Black"))
            self.add_card(Card(value, "Clove", "Black"))
# segundo
    def shuffle_deck(self):
        for i in range(1000):
            ra = random.randint(0, len(self.cards) - 1)
            rb = random.randint(0, len(self.cards) - 1)
            self.swap_cards_in_deck(ra,rb)
# si la tiene el usuario
    def remove_card(self, card_index: int) -> bool:
        if 0 <= card_index < len(self.cards):
            self.cards.pop(card_index)
            return True
        return False

    def index_of_card(self, number: int, suit: str) -> int:
        for i in range(len(self.cards)):
            card = self.cards[i]
            if card.number == number and card.suit == suit:
                return i
        return -1
# si tiene la carta
    def contains_card(self, number: int, suit: str) -> bool:
        return self.index_of_card(number, suit) >= 0 
# para repartir una carta
    def pick_up_card(self) -> Card:
        if not self.cards:
            return None
        C = self.cards[0]
        self.cards.pop(0)
        return C
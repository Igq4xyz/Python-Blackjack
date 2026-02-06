from dataclasses import dataclass
from Card import Card

@dataclass
class Player:
    name: str
    score_limit: int
    cards: list = list[Card]
    stand: bool = False



    def add_card (self, card: Card):
        if card:
            self.cards.append(card)
    
    def calculate_score(self) -> int:
        total = 0
        for card in self.cards:
            total += card.number
        return total
    
    def wants_card(self) -> bool:
        if self.calculate_score() < self.score_limit:
            return True
        return False

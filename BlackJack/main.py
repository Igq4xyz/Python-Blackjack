from dataclasses import dataclass
from Card import Card
from  Deck import Deck
from Player import Player


deck = Deck([])
deck.init_deck()
deck.shuffle_deck()

banca = Player("Banca", 17, [], False)
player1 = Player("Pedro", 18, [], False)
 
player1.add_card(deck.pick_up_card())
player1.add_card(deck.pick_up_card())
banca.add_card(deck.pick_up_card())
banca.add_card(deck.pick_up_card())

print("Cartas Pedro:", player1.cards)
print("Cartas banca:", banca.cards)

# Turno del jugador
while player1.wants_card():
    player1.add_card(deck.pick_up_card())
    print("Pedro roba:", player1.cards[-1])
    print("Puntos Pedro:", player1.calculate_score())

# Turno de la banca
while banca.wants_card():
    banca.add_card(deck.pick_up_card())
    print("Banca roba:", banca.cards[-1])
    print("Puntos banca:", banca.calculate_score())


player_score = player1.calculate_score()
banca_score = banca.calculate_score()

print("Pedro:", player_score)
print("Banca:", banca_score)

if player_score > 21:
    print("Pedro se pasa. Gana la banca.")
elif banca_score > 21:
    print("La banca se pasa. Gana el jugador.")
elif banca_score and player_score > 21:
    print("Los dos se pasan, no gana nadie")
elif player_score > banca_score:
    print("Gana Pedro")
elif banca_score > player_score:
    print("Gana banca")
elif banca_score == player_score:
    print("Los dos empatan")
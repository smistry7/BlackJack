import pydealer
import sys
import time
import Player

ranks = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def main():
    play = True
    while play:
        player_name = input("Please enter your name")
        player = Player.Player(player_name)
        deck = pydealer.Deck()
        deck.shuffle()
        dealer_hand = deck.deal(2)
        dealer_up_card = dealer_hand[0]
        player_hand = deck.deal(2)

        print("Dealer Up card: " + str(ranks[dealer_up_card.value]))
        print("Player Hand: " + str(player_hand) + "\nvalue: " +
              str(hand_value(player_hand)))
        hit_response = query_player(dealer_hand, deck, player_hand)
        while hit_response != "h" and hit_response != "s":
            hit_response = query_player(dealer_hand, deck, player_hand)
        while hit_response == "h":
            player_hand += deck.deal(1)
            print(str(player_hand))
            value = hand_value(player_hand)
            print("Value: " + str(value))
            if value > 21:
                print("BUST, YOU LOSE")
                player.update_record(player_name, False)
                sys.exit()
            hit_response = input("hit(h) or stick(s)?       blackjack probability="
                                 + str(blackjack_probability(player_hand, dealer_hand))
                                 + "     bust probability =" + str(bust_probability(player_hand, deck)))
        print("Dealer hand: " + str(dealer_hand))
        print("value: " + str(hand_value(dealer_hand)))
        no_winner = True
        while no_winner:
            time.sleep(2)
            if hand_value(dealer_hand) > hand_value(player_hand):
                print("Dealer Wins!")
                player.update_record(player_name, False)
                no_winner = False
            elif hand_value(dealer_hand) > hand_value(player_hand) & hand_value(dealer_hand) > 16:
                print("Player Wins!")
                player.update_record(player_name, True)
                no_winner = False
            else:
                dealer_hand += deck.deal(1)
                if hand_value(dealer_hand) > 21:
                    print("Player Wins!")
                    player.update_record(player_name, True)
                    no_winner = False
            print("Dealer Hand: " + str(dealer_hand))
            print("value: " + str(hand_value(dealer_hand)))
        play_response = input("play again? y/n")
        if play_response == "y":
            play = True
        else:
            play = False


def query_player(dealer_hand, deck, player_hand):
    return input("hit(h) or stick(s)?         blackjack probability="
                 + str(blackjack_probability(player_hand, dealer_hand))
                 + "     bust probability =" + str(bust_probability(player_hand, deck)))


def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        value += ranks[card.value]
        if card.value == "Ace":
            aces += 1
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    return value


def blackjack_probability(player_hand, dealer_hand):
    value_needed = 21 - hand_value(player_hand)
    if value_needed == 0:
        return 1
    num_showing = len(player_hand) + len(dealer_hand)
    if value_needed > 11:
        return 0
    num_needed_showing = 0
    for i in player_hand:
        if ranks[i.value] == value_needed:
            num_needed_showing += 1

    if ranks[dealer_hand[0].value] == value_needed:
        num_needed_showing += 1

    if value_needed != 10:
        prob_value_needed = (4 - num_needed_showing) / (52 - num_showing)
        return prob_value_needed
    if value_needed == 10:
        prob_value_needed = (16 - num_needed_showing) / (52 - num_showing)
        return prob_value_needed


def bust_probability(player_hand, deck):
    value_needed = 21 - hand_value(player_hand)
    if value_needed == 0:
        return 1
    num_busts = 0
    for card in deck:
        if (ranks[card.value] > value_needed) & (str(card.value) != "Ace"):
            num_busts += 1
    bust_prob = num_busts / len(deck)
    return bust_prob


if __name__ == "__main__": main()

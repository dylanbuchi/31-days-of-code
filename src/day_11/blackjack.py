# Blackjack
import sys
import os
import random
from colorama import init, Fore
from time import sleep

from logo import LOGO


def create_standard_deck():
    """Create a deck of cards with 8 packs"""
    deck = []
    for _ in range(8):
        cards = {i: i for (i) in range(2, 11)}
        cards.update({'J': 10, 'Q': 10, 'K': 10, 'A': [11, 1]})
        deck.append(cards)
    return deck


def refill_deck(deck):
    if not deck:
        temp = create_standard_deck()
        deck.extend(temp)


def get_a_card(card_names, card_values, cards_count):
    """get a random card with it's value and remove it from deck"""
    index = random.randrange(0, len(card_names))
    card_name, card_value = card_names[index], card_values[index]

    cards_count[card_name] += 1

    if cards_count[card_name] == 4:
        card_names.pop(index)
        card_values.pop(index)

    return card_name, card_value


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_value_for_Ace_card(player_name, player_card, card_values, total=0):
    """return 1 or 11 if card is As"""
    if (player_card != 'A'):
        return

    if player_name == 'You':
        try:

            choice = int(
                input("Your card is an Ace Do you want 1 or 11?:\n ").lower().
                strip())
            assert choice == 1 or choice == 11

        except (ValueError, AssertionError):
            print("Error, pick 1 or 11!")
            return get_value_for_Ace_card(player_name, player_card,
                                          card_values)

        else:
            clear_console()
            return choice
    else:
        bot_choice = 11 if total < 17 else 1
        return bot_choice


def print_result(player_name, current_hand, total):
    total_color = Fore.RED if total > 21 else Fore.YELLOW

    print("*" * 80, end="\n")
    print(f"{Fore.GREEN} {player_name.upper()}:\n")

    print(f"Cards: {Fore.YELLOW + ', '.join(current_hand)}\n")
    print(f"Total: {total_color + str(total)}\n")


def draw_card(player_name,
              card_names,
              card_values,
              current_hand,
              total,
              cards_count,
              balance=0):
    """A player draws a card, prints their hand and return the total points"""
    card, card_value = get_a_card(card_names, card_values, cards_count)
    if card != 'A':
        total += card_value
    else:
        if player_name != 'The dealer':
            if (total):
                print_result(player_name, current_hand, total)

        total += get_value_for_Ace_card(player_name, card, card_value, total)
        # if player_name == 'The dealer':
        #     print_result(player_name, current_hand, total)

    # print("*" * 80, end="\n")
    # print(f"{player_name.upper()}:\n")

    current_hand.append(f"[{str(card)}]")

    # print_result(player_name, current_hand, total)

    return total


def print_player_balance(balance):
    print(f"you have ${Fore.GREEN + str(balance)}")


def rules(player_total, dealer_total, player_stop_draw):
    win = None
    if (player_total == 21):
        win = True
    elif (dealer_total == 21):
        win = False
    elif dealer_total >= 22:
        win = True
    elif player_total >= 22:
        win = False

    if player_stop_draw:
        if (player_total >= dealer_total and player_total < 21):
            win = True
        elif (dealer_total > player_total and dealer_total < 21):
            win = False
    return win


def place_bet(max):

    try:
        bet = int(input("Place your bet\n:$"))
        assert bet > 0 and bet <= max
    except (AssertionError, ValueError):
        print("Place a correct bet amount")
        return place_bet(max)
    else:
        clear_console()
        return bet


def dealer_plays(dealer_name, card_names, card_values, dealer_hand,
                 dealer_total, player_total, cards_count):

    while True:
        if dealer_total >= 17 and player_total <= 17:
            return dealer_total
        else:
            if dealer_total > 21:
                break
            dealer_total = draw_card(dealer_name, card_names, card_values,
                                     dealer_hand, dealer_total, cards_count)

        print_result(dealer_name, dealer_hand, dealer_total)
        sleep(1.2)
        clear_console()
    return dealer_total


def hit_or_stand():
    try:
        answer = int(input(" Hit (1) or Stand (2)\n:").lower().strip())
        assert 1 <= answer <= 2
    except (AssertionError, ValueError):
        print(f"Enter 1 to Hit or 2 to Stand")
        return hit_or_stand()
    return answer


def get_cards():
    cards = {i: i for (i) in range(1, 11)}
    cards.update({'J': 10, 'Q': 10, 'K': 10, 'A': [11, 1]})
    return cards


def play_black_jack(decks):

    # variables
    game_ended = False
    only_dealer_plays = False
    player_stop_draw = False
    new_game = True

    player_name = 'You'
    balance = 100
    dealer_name = 'The dealer'

    player_hand = []
    dealer_hand = []
    cards_count = get_cards()
    for k, v in cards_count.items():
        cards_count[k] = 0

    player_total = dealer_total = bet = 0

    while (len(decks)):
        current_deck = decks.pop()

        card_names = list(current_deck.keys())
        card_values = list(current_deck.values())

        # while current deck has cards
        while (len(card_names) and len(card_values)):
            if (balance <= 0):
                print("You have $0, deposit more to play again!")
                sys.exit()

            if new_game:
                new_game = False
                print_player_balance(balance)
                bet = place_bet(balance)
                dealer_total = draw_card(dealer_name, card_names, card_values,
                                         dealer_hand, dealer_total,
                                         cards_count)

            if only_dealer_plays:

                dealer_total = dealer_plays(dealer_name, card_names,
                                            card_values, dealer_hand,
                                            dealer_total, player_total,
                                            cards_count)
            else:

                print_result(dealer_name, dealer_hand, dealer_total)
                player_total = draw_card(player_name, card_names, card_values,
                                         player_hand, player_total,
                                         cards_count, balance)

                print_result(player_name, player_hand, player_total)

            has_winner = rules(player_total, dealer_total, player_stop_draw)

            if (has_winner == None):
                answer = ''

                if (not only_dealer_plays):
                    answer = hit_or_stand()

                if answer == 1:
                    clear_console()
                    continue
                else:
                    clear_console()
                    player_stop_draw = True
                    only_dealer_plays = True
                    continue

            elif (has_winner):
                clear_console()

                balance += bet * 2

                print_result(dealer_name, dealer_hand, dealer_total)
                print_result(player_name, player_hand, player_total)
                if player_total == 21:
                    print(f"{Fore.CYAN} BLACKJACK ", end='')
                print(f"You Win! {Fore.GREEN}+${bet * 2}")
                game_ended = True
                break
            elif (has_winner == False):
                clear_console()

                game_ended = True
                balance -= bet
                print_result(dealer_name, dealer_hand, dealer_total)
                print_result(player_name, player_hand, player_total)
                if (dealer_total == 21):
                    print(f"{Fore.CYAN} BLACKJACK ", end='')
                print(f"Dealer wins! {Fore.RED} -${bet}\n")
                break

        # clear the current deck adn count when cards are empty
        if (not len(card_names) and not len(card_values)):
            current_deck.clear()
            cards_count.clear()

        # check if it's the end game
        if (game_ended):
            player_total, dealer_total = reset_points()
            reset_player_hand(player_hand)
            reset_player_hand(dealer_hand)

            ans = input("play again ? (y/n)\n:")

            if (ans == 'y'):
                game_ended = False
                only_dealer_plays = False
                player_stop_draw = False
                new_game = True
                clear_console()
                continue
            else:
                return
            # refill if no more cards in the decks
    if (not decks):
        refill_deck(decks)
        play_black_jack()


def reset_player_hand(player_hand):
    player_hand.clear()


def reset_points():
    return 0, 0


def user_interface():
    decks = create_standard_deck()
    play_black_jack(decks)


def main():
    init(autoreset=True)
    print(LOGO)

    try:
        user_interface()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
import random
# ♥ ♠ ♦ ♣
DeckOfCards = ["A♣","2♣", "3♣" ,"4♣" ,"5♣", "6♣" , "7♣" , "8♣" , "9♣", "10♣" , "J♣" , "Q♣" , "K♣","A♦","2♦" ,"3♦" ,"4♦" ,"5♦", "6♦" , "7♦" , "8♦" , "9♦", "10♦" , "J♦" , "Q♦" , "K♦","A♠","2♠", "3♠" ,"4♠" ,"5♠", "6♠" , "7♠" , "8♠" , "9♠", "10♠" , "J♠" , "Q♠" , "K♠" , "A♥","2♥", "3♥" ,"4♥" ,"5♥", "6♥" , "7♥" , "8♥" , "9♥", "10♥" , "J♥" , "Q♥" , "K♥"]

def card_points(card):
    if card.startswith('A'):
        return 11  
    elif card in ['J♣', 'J♦', 'J♠', 'J♥', 'Q♣', 'Q♦', 'Q♠', 'Q♥', 'K♣', 'K♦', 'K♠', 'K♥']:
        return 10  
    else:
        return int(card[:-1])
        
def total_hand_value(hand):
    total = sum(card_points(card) for card in hand)
    ace_count = hand.count("A♣") + hand.count("A♦") + hand.count("A♠") + hand.count("A♥")
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

def play_blackjack():
    print("Welcome to Josh's (Probably Rigged) BlackJack!")
    player_name = input("What is your name? ")
    player_money = 1000
    
    while player_money > 0:
        print(f"\nYou have ${player_money}.")
        bet = int(input("Place your bet (min $5, max $100): $"))
        
        while bet < 5 or bet > 100 or bet > player_money:
            bet = int(input("Invalid bet. Please place a valid bet: $"))
            
        player_hand = [random.choice(DeckOfCards), random.choice(DeckOfCards)]
        dealer_hand = [random.choice(DeckOfCards), random.choice(DeckOfCards)]
        
        print(f"\n{player_name}'s cards: {player_hand}(total: {total_hand_value(player_hand)})")
        print(f"\nDealer's visible card: {dealer_hand[0]}")  
        
        while total_hand_value(player_hand) <= 21:
            action = input("Do you want to hit (h) or stand (s)? ")
            
            if action == 'h':
                player_hand.append(random.choice(DeckOfCards))
                print(f"\n{player_name}'s cards: {player_hand} (total: {total_hand_value(player_hand)})")
                
            elif action == 's':
                break
        
        player_total = total_hand_value(player_hand)
        
        if player_total > 21:
            print("You Busted :(")
            player_money -= bet
            continue
        
        dealers_total_one = total_hand_value(dealer_hand)
        print(f"\nDealer's cards: {dealer_hand} (total: {dealers_total_one})")
        
        while total_hand_value(dealer_hand) < 17:
            dealer_hand.append(random.choice(DeckOfCards))
            
            dealers_total_two = total_hand_value(dealer_hand)
            print(f"Dealer hits: {dealer_hand} (total: {dealers_total_two})")
            
        dealer_total = total_hand_value(dealer_hand)
        print(f"Final totals - {player_name}: {player_total}, Dealer: {dealer_total}")

        if dealer_total > 21 or player_total > dealer_total:
            print("You win!")
            player_money += bet
        elif player_total < dealer_total:
            print("You lose.")
            player_money -= bet
        else:
            print("It's a tie! Your bet is returned.")

        if player_money == 0:
            print("You have run out of money! Game over.")
            break
    
    print("Thanks for playing!")


play_blackjack()
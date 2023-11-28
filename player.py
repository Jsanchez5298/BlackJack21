# player.py

class Player:
    #Initialize the player's hand.
    def __init__(self):
        self.hand = []

    #Add a card to the player's hand.
    def draw_card(self, card):
        self.hand.append(card)  # Add the card to the hand

    #Calculate the value of the player's hand, accounting for aces.
    def get_hand_value(self):
        hand_value = sum(card.value for card in self.hand)  # Sum the value of the cards in the hand
        num_aces = sum(1 for card in self.hand if card.rank == "Ace")   # Count the number of aces in the hand

        # Adjust for aces to maximize the hand value
        while hand_value > 21 and num_aces: # If the hand value is greater than 21 and there are aces in the hand
            hand_value -= 10  # Convert Ace from 11 to 1
            num_aces -= 1   # Decrement the number of aces in the hand

        return hand_value   # Return the hand value

    #Placeholder for player action handling. You might implement logic to handle 'hit' or 'stand' actions here.
    #def take_action(self, mouse_pos, deck):
        #Here you might implement how a player would decide to 'hit' or 'stand' based on game logic or user input
        # For instance:
        # while player_input != 'stand':
        #    if player_input == 'hit':
        #        self.draw_card(deck.deal_card())
        #    player_input = input("Do you want to hit or stand? ")

        #if self.hit_button.collidepoint(mouse_pos):
           # self.player.draw_card(deck.deal_card())
       # elif self.stand_button.collidepoint(mouse_pos):
           # pass
            # Player stands, move to dealer's turn
            # Implement dealer's logic or update game state accordingly




    #Reset the player's hand for a new round.
    def reset_hand(self):
        self.hand = []
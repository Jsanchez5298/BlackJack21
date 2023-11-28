# dealer.py

# class represents the dealer, allowing you to build a hand, draw cards, and make decisions on hitting or standing.
class Dealer:
    #Initialize the dealer's hand and a variable to store the hidden card.
    def __init__(self):
        self.hand = []
        self.hidden_card = False

    #Add a card to the dealer's hand
    def draw_card(self, card):
        self.hand.append(card)  # Add the card to the hand

    #Make the dealer's decision on hitting or standing.
    def take_action(self, deck):
        hand_value = self.get_hand_value()  # Get the value of the dealer's hand

        while hand_value < 17:  # Dealer must hit if hand value is less than 17
            self.draw_card(deck.deal_card())    # Draw a card from the deck
            hand_value = self.get_hand_value()  # Update the hand value

    #Calculate the value of the dealer's hand, accounting for aces.
    def get_hand_value(self):
        hand_value = sum(card.value for card in self.hand)  # Sum the value of the cards in the hand
        num_aces = sum(1 for card in self.hand if card.rank == "Ace")   # Count the number of aces in the hand

        # Adjust for aces to maximize the hand value
        while hand_value > 21 and num_aces: # If the hand value is greater than 21 and there are aces in the hand
            hand_value -= 10  # Convert Ace from 11 to 1
            num_aces -= 1   # Decrement the number of aces in the hand

        return hand_value   # Return the hand value

    #Reset the dealer's hand and hidden card for a new round.
    def reset_hand(self):
        self.hand = []


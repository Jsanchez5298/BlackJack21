# event_handler.py
import pygame
from dealer import Dealer
from player import Player
from deck import Deck


class EventHandler:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Creating the game window
        # resets the screen
        self.screen.fill((0, 128, 0))  # Background color

        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

        self.hit_button = pygame.Rect(50, 500, 100, 50)  # x, y, width, height
        self.stand_button = pygame.Rect(200, 500, 100, 50)
        self.quit_button = pygame.Rect(350, 500, 100, 50)

        # Draw 'Hit' and 'Stand' buttons and 'Quit' button
        pygame.draw.rect(self.screen, (0, 255, 0), self.hit_button)
        pygame.draw.rect(self.screen, (255, 0, 0), self.stand_button)
        pygame.draw.rect(self.screen, (0, 0, 255), self.quit_button)

        # Define the font
        self.font = pygame.font.Font(None, 36)

        # Render text on buttons
        hit_text = self.font.render("Hit", True, (255, 255, 255))
        stand_text = self.font.render("Stand", True, (255, 255, 255))
        quit_text = self.font.render("Quit", True, (255, 255, 255))

        # Center the text on buttons
        hit_text_rect = hit_text.get_rect(center=self.hit_button.center)
        stand_text_rect = stand_text.get_rect(center=self.stand_button.center)
        quit_text_rect = quit_text.get_rect(center=self.quit_button.center)

        # Blit the text onto the screen
        self.screen.blit(hit_text, hit_text_rect)
        self.screen.blit(stand_text, stand_text_rect)
        self.screen.blit(quit_text, quit_text_rect)

        pygame.display.set_caption("Blackjack")  # Setting the window title]
        
    def start_game(self):
        gameClock = pygame.time.Clock()
        running = True
        while running:
            self.handle_events()  # just for quitting with x
            # pygame.display.flip()   #refreshes the screen
            self.update_game_state()
            self.render()
            # pygame.display.flip()   #refreshes the screen

            gameClock.tick(10)

        # pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handling the window close event (clicking the 'X' button)
                pygame.quit()
                quit()  # Exiting the game loop and the program

            # Other event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handling mouse clicks
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the click was on a specific button or game element

    def display_message(self, message):
        # Clear the message area
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 240, 800, 65))

        self.font = pygame.font.Font(None, 65)
        text = self.font.render(message, True, (255, 0, 0))
        self.screen.blit(text, (200, 240))
        pygame.display.flip()
        pygame.time.delay(1500)

    def update_game_state(self):
        # Check for game end conditions or player actions to update game state
        self.deck.reset_deck()
        self.player.reset_hand()
        self.dealer.reset_hand()

        # Deal initial cards
        if len(self.player.hand) == 0 and len(self.dealer.hand) == 0:
            for _ in range(2):
                self.player.draw_card(self.deck.deal_card())
                self.dealer.draw_card(self.deck.deal_card())
            # self.dealer.hidden_card = self.dealer.hand[1]  # Hide dealer's second card

        self.render()
        # Update the display
        pygame.display.flip()  # refreshes the screen

        # Check for player's turn
        turn = True
        while turn and len(self.player.hand) > 0:
            if len(self.player.hand) > 0:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if (self.stand_button.collidepoint(mouse_pos)):
                            # self.dealer.reveal_card()
                            self.dealer.take_action(self.deck)
                            self.render()
                            pygame.display.flip()
                            turn = False
                        elif (self.hit_button.collidepoint(mouse_pos)):
                            if self.player.get_hand_value() > 21:
                                self.render()
                                turn = False
                            else:
                                self.player.draw_card(self.deck.deal_card())
                                self.render()
                            # Update the display
                            pygame.display.flip()
                        elif (self.quit_button.collidepoint(mouse_pos)):
                            pygame.quit()
                            quit()

        # Check for game outcomes
        if self.player.get_hand_value() > 21:
            print("Player busts!")
            self.display_message("Player busts!")
            # Handle other win/lose conditions and game state updates
            if self.dealer.get_hand_value() > 21:
                print("Dealer busts! Draw!")
                self.display_message("Dealer busts! Draw!")
            else:
                print("Dealer wins!")
                self.display_message("Dealer wins!")

        elif self.player.get_hand_value() == 21:
            if self.dealer.get_hand_value() != 21:
                print("Player wins!")
                self.display_message("Player wins!")
            else:
                print("Draw!")
                self.display_message("Draw!")

        elif self.player.get_hand_value() < 21:
            if self.dealer.get_hand_value() > 21:
                print("Dealer busts! Player wins!")
                self.display_message("Dealer busts! Player wins!")
            elif self.dealer.get_hand_value() == 21:
                print("Dealer wins!")
                self.display_message("Dealer wins!")
            elif self.dealer.get_hand_value() < 21:
                if self.player.get_hand_value() > self.dealer.get_hand_value():
                    print("Player wins!")
                    self.display_message("Player wins!")
                elif self.player.get_hand_value() < self.dealer.get_hand_value():
                    print("Dealer wins!")
                    self.display_message("Dealer wins!")
                elif self.player.get_hand_value() == self.dealer.get_hand_value():
                    print("Draw!")
                    self.display_message("Draw!")

    def render(self):
        # resets the screen
        self.screen.fill((0, 128, 0))  # Background color

        # Draw 'Hit' and 'Stand' buttons and 'Quit' button
        pygame.draw.rect(self.screen, (0, 255, 0), self.hit_button)
        pygame.draw.rect(self.screen, (255, 0, 0), self.stand_button)
        pygame.draw.rect(self.screen, (0, 0, 255), self.quit_button)

        # Define the font
        self.font = pygame.font.Font(None, 36)

        # Render text on buttons
        hit_text = self.font.render("Hit", True, (255, 255, 255))
        stand_text = self.font.render("Stand", True, (255, 255, 255))
        quit_text = self.font.render("Quit", True, (255, 255, 255))

        # Center the text on buttons
        hit_text_rect = hit_text.get_rect(center=self.hit_button.center)
        stand_text_rect = stand_text.get_rect(center=self.stand_button.center)
        quit_text_rect = quit_text.get_rect(center=self.quit_button.center)

        # Blit the text onto the screen
        self.screen.blit(hit_text, hit_text_rect)
        self.screen.blit(stand_text, stand_text_rect)
        self.screen.blit(quit_text, quit_text_rect)

        # Display player's hand
        player_hand_text = ", ".join([card.rank + ' of ' + card.suit for card in self.player.hand])
        print(player_hand_text)
        player_text_surface = pygame.font.Font(None, 36).render(f"Player's Hand: {player_hand_text}", True, (255, 255, 255))
        overlap = 35  # Adjust this value based on how much overlap you want

        # Display the first card
        self.screen.blit(self.player.hand[0].image, (20, 200))

        # Loop for the rest of the cards
        for i in range(1, len(self.player.hand)):
            self.screen.blit(self.player.hand[i].image, (20, 200 + i * overlap))

        self.screen.blit(player_text_surface, (20, 20))

        # Display dealer's hand (showing the hidden card)
        dealer_hand_text = ", ".join([card.rank + ' of ' + card.suit for card in self.dealer.hand])
        if len(self.dealer.hand) > 1:
            dealer_text_surface = pygame.font.Font(None, 36).render(f"Dealer's Hand: {dealer_hand_text}", True,
                                                                    (255, 255, 255))
            self.screen.blit(dealer_text_surface, (20, 80))
            print(dealer_hand_text)
            # load and draw the dealer's cards
            self.screen.blit(self.dealer.hand[0].image, (220, 200))

            # Loop for the rest of the cards
            for i in range(1, len(self.dealer.hand)):
                self.screen.blit(self.dealer.hand[i].image, (220, 200 + i * overlap))

        # Update the display
        pygame.display.flip()
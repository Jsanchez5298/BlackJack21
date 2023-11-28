# BlackJack21

### Submitted by: Jose Sanchez | Nov 21, 2023

A command-line based download using Python implementing Object Oriented Programming.
The game runs slow so overtapping on the buttons is not recomendded.

### Installing BlackJack21

> git clone https://github.com/Jsanchez5298/BlackJack21.git
> Create a virtual env
> import pygame
> In command-line run python main.py and enjoy!


### Objective of the game
The player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
Shows the player how levels of learning blackjack is fun.

### Card values
- An ace is worth 1 or 11. 
- Face cards are 10
- Any other card is its num value.

### Game key terms
- Hit: To 'Hit' is to ask for another card. 
- Stand: To 'Stand' is to hold your total and end your turn.
- Bust: If your card total goes over 21 you bust, and the dealer wins regardless of the dealer's hand.

### Initial Deal
As a single player you start with two cards, and you have an advatage as you see the dealer's inital two cards.

### Hitting
After the first round of dealing, you as the player has the option to click the hit button (adds one more card/cards). If hitting results in busting (total going over 21), then his or her game is lost.

### Standing
After player has clicked on stand button (no more cards). If the dealer’s total is less than 17, then the dealer hits the deck (adds a new card). This process repeats until the dealer’s hand either totals to 17 or more or busts (goes above 21). The game checks who wins the round.

### ReDealing 
After the game results are outputted on the screen the game takes about five seconds to render the player's and dealer's next hand from the same game deck. The player then plays blackjack21 against the dealer again.

### Quiting
If the player is done playing they can simply click the quit button and the game will exit.

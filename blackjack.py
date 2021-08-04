import random
import time



#Deck of 52 cards
card_deck = [
"1a","1b","1c","1d",    # a = diamonds
"2a","2b", "2c", "2d",	# b = clubs
"3a","3b", "3c", "3d",	# c = heart
"4a","4b", "4c", "4d",	# d = spade
"5a","5b", "5c", "5d",
"6a","6b", "6c", "6d",
"7a","7b", "7c", "7d",
"8a","8b", "8c", "8d",
"9a","9b", "9c", "9d",
"10a","10b", "10c", "10d",
"11a","11b", "11c", "11d",
"12a","12b", "12c", "12d",
"13a","13b", "13c", "13d",
]

#Dictionary containing the name and value of cards
card_dict = { 
"1a" : ["Ace of Diamond",11],
"1b" : ["Ace of Clubs",11], 
"1c" : ["Ace of Heart",11], 
"1d" : ["Ace of Spades",11],
"2a" : ["Two of Diamond",2],
"2b" : ["Two of Clubs",2], 
"2c" : ["Two of Heart",2], 
"2d" : ["Two of Spades",2],
"3a" : ["Three of Diamond",3],
"3b" : ["Three of Clubs",3], 
"3c" : ["Three of Heart",3], 
"3d" : ["Three of Spades",3],
"4a" : ["Four of Diamond",4],
"4b" : ["Four of Clubs",4], 
"4c" : ["Four of Heart",4], 
"4d" : ["Four of Spades",4], 
"5a" : ["Five of Diamond",5],
"5b" : ["Five of Clubs",5], 
"5c" : ["Five of Heart",5], 
"5d" : ["Five of Spades",5],
"6a" : ["Six of Diamond",6],
"6b" : ["Six of Clubs",6], 
"6c" : ["Six of Heart",6], 
"6d" : ["Six of Spades",6], 
"7a" : ["Seven of Diamond",7],
"7b" : ["Seven of Clubs",7], 
"7c" : ["Seven of Heart",7], 
"7d" : ["Seven of Spades",7],
"8a" : ["Eight of Diamond",8],
"8b" : ["Eight of Clubs",8], 
"8c" : ["Eight of Heart",8], 
"8d" : ["Eight of Spades",8], 
"9a" : ["Nine of Diamond",9],
"9b" : ["Nine of Clubs",9], 
"9c" : ["Nine of Heart",9], 
"9d" : ["Nine of Spades",9],
"10a" : ["Ten of Diamond",10],
"10b" : ["Ten of Clubs",10], 
"10c" : ["Ten of Heart",10], 
"10d" : ["Ten of Spades",10], 
"11a" : ["Jack of Diamond",10],
"11b" : ["Jack of Clubs",10], 
"11c" : ["Jack of Heart",10], 
"11d" : ["Jack of Spades",10],
"12a" : ["Queen of Diamond",10],
"12b" : ["Queen of Clubs",10], 
"12c" : ["Queen of Heart",10], 
"12d" : ["Queen of Spades",10],  
"13a" : ["King of Diamond",10],
"13b" : ["King of Clubs",10], 
"13c" : ["King of Heart",10], 
"13d" : ["King of Spades",10]
}

#Player class
class Player:
	"""
	BlackJack Player Class

	Parameters:
	name = name of player 
	"""
	def __init__(self, name):
		self.name = name
		self.points = 0
		self.cards = []
		self.aces = 0
		self.cont = 1 # continue game or not

	#Draw a card FUNCTION
	def draw_card(self, deck=card_deck, dictionary=card_dict, reveal="shown"):
		"""
		 A function to draw cards from the card deck.
		 note: this function requires the time.sleep function of time library
		 MAKE SURE TO import time.
		 
		 Parameters:
		 deck = list where the card is drawn from.
		 dictionary = the dictionary containing name & value of cards.
		 reveal = whether the card drawn will be "shown" or "hidden".

		""" 
		card_taken = deck[random.randint(0,len(deck)-1)]
		if card_taken in ["1a", "1b", "1c", "1d"]:
			self.aces += 1
		card_name = dictionary[card_taken][0]
		self.cards.append(card_taken)
		self.points += int(dictionary[card_taken][1])
		deck.remove(card_taken)
		time.sleep(1)
		if reveal == "shown":
			print(f"{self.name} has drawn the {card_name}.")
		elif reveal == "hidden":
			print(f"{self.name} has drawn a card (Hidden).")

	#Convert Ace value from 11 to 1 FUNCTION
	def convert_ace_check(self):
		""" 
		A function that checks whether player has an ace card or not, 
		then converts the point value of Ace from 11 to 1.
		"""
		if self.aces > 0:
			self.points -= 10
			self.aces -= 1
		else:
			self.cont = 0

# player1 = Player("Edbert Ekaputera")

# player1.draw_card(card_deck, card_dict, "shown")
# player1.draw_card(card_deck, card_dict, "shown")
# player1.draw_card(card_deck, card_dict, "hidden")

# print(player1.cards)
# print(player1.points)
# print(card_deck) 

#Start of the game
if __name__ == "__main__":
	print("Welcome to BLACKJACK!")
	player1 = Player(str(input("What is your name? ")))
	dealer = Player("Dealer")
	while True:
		print("Would you like to play a game of BlackJack? \n1 : Yes\n2 : No")
		start_game = str(input("Answer = "))
		if start_game == "1":
			break
		elif start_game == "2":
			print("Okay... Have a great day.")
			exit()
		else:
			print("That wasn't an appropriate answer...\n")

	player_continue = 1
	print(f"\nDealer : Good day to you, {player1.name}.\nDealer : Today I will be your Dealer.")
	print("Dealer : I will now draw the starting cards...")
	#starting cards (two shown cards for player; 1 shown card,1 hidden card for dealer)
	player1.draw_card(card_deck, card_dict, "shown")
	dealer.draw_card(card_deck, card_dict, "hidden")
	player1.draw_card(card_deck, card_dict, "shown")
	dealer.draw_card(card_deck, card_dict, "shown")
	time.sleep(1)

	while player1.cont == 1:
		if player1.points == 21: #Black Jack
			while dealer.cont == 1:
				if dealer.points < 17:
					dealer.draw_card(card_deck, card_dict, "shown")
				elif dealer.points >= 17:
					if dealer.points > 21: #BUST
						dealer.convert_ace_check() #check if Ace can be converted from 11 to 1
					else:
						dealer.cont = 0
			break
		print(f"\nYou currently have a total of {player1.points}. \nWould you like to HIT? \n1 : Yes\n2 : No")
		hit_continue = str(input("Answer = "))
		if hit_continue == "2":
			while dealer.cont == 1:
				if dealer.points < 17:
					dealer.draw_card(card_deck, card_dict, "shown")
				elif dealer.points >= 17:
					if dealer.points > 21: #BUST
						dealer.convert_ace_check() #check if Ace can be converted from 11 to 1
					else:
						dealer.cont = 0
			player1.cont = 0

		elif hit_continue == "1":
			player1.draw_card(card_deck, card_dict, "shown")
			if player1.points > 21: #Bust
				player1.convert_ace_check()
			if dealer.points < 17 and player1.points < 21:
				dealer.draw_card(card_deck, card_dict, "shown")
				if dealer.points > 21: #Bust
					dealer.convert_ace_check()
					if dealer.cont == 0:
						break
				
	#Win/Lose Condition
	print("\n")
	if player1.points == 21 and dealer.points != 21:
		print("BLACKJACK!!! CONGRATULATIONS YOU HAVE WON!")
	elif dealer.points == 21 and player1.points != 21:
		print("UNLUCKY! THE DEALER GOT A BLACKJACK!")
	elif player1.points > 21:
		print("AWW! YOU HAVE LOST!")
		print(f"Your {player1.points} have busted over 21")
	elif dealer.points > 21:
		print("LUCKY! YOU HAVE WON!")
		print(f"The dealer's {dealer.points} have busted over 21")
	elif player1.points > dealer.points:
		print("CONGRATULATIONS YOU HAVE WON!")
		print(f"Your {player1.points} has beaten the dealer's {dealer.points}.")
	elif player1.points < dealer.points:
		print("AWW! YOU HAVE LOST!")
		print(f"The dealer's {dealer.points} has beaten your {player1.points}.")
	elif player1.points == dealer.points:
		print("IT'S A DRAW!")
		print(f"Both you and the dealer have the total of {player1.points}.")











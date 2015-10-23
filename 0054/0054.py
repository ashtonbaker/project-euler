import math
import time

start_time = time.time()

def card_value(card):
	card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	return card_order.index(card[0])

def suit_value(card):
	suit_order = ['D', 'S', 'H', 'C']
	return suit_order.index(card[1])

def test_hand(hand):
	sorted_hand = sorted(hand, key = card_value)
	cards = [0] * 13
	suits = [0] * 4

	for card in sorted_hand:
		cards[card_value(card)] += 1
		suits[suit_value(card)] += 1

	# Royal Flush / Straight Flush
	if 5 in suits: # Then we have a flush
		if sorted_hand[0][0] == 'T': # Then we have a royal flush
			return [10, sorted_hand]
		elif card_value(sorted_hand[4]) - card_value(sorted_hand[0]) == 4: # Straight Flush
			return [9, sorted_hand]

	# Four of a kind
	if max(cards) == 4:
		return [8, [card_value(card) for card in sorted_hand]]

	# Full House
	if (3 in cards) and (2 in cards):
		return [7, [card_value(card) for card in sorted_hand]]

	# Flush
	if 5 in suits:
		return [6, [card_value(card) for card in sorted_hand]]

	# Straight
	if card_value(sorted_hand[4]) - card_value(sorted_hand[0]) == 4:
		return [5, [card_value(card) for card in sorted_hand]]

	# 3 of a kind
	if 3 in cards:
		return [4, [card_value(card) for card in sorted_hand]]

	# 2 pairs
	if len([i for i,x in enumerate(cards) if x == 2]) == 2:
		return [3, [card_value(card) for card in sorted_hand]]

	# 1 pair
	if 2 in cards:
		return [2, [card_value(card) for card in sorted_hand]]

	# High card
	return [1, [card_value(card) for card in sorted_hand]]

def compare_hands(hand_1, hand_2):
	if   hand_1[0] > hand_2[0]:
		return 1
	elif hand_1[0] < hand_2[0]:
		return 2
	else:
		for i in range(5):
			if hand_1[1][4 - i] > hand_2[1][4 - i]:
				return 1
			elif hand_1[1][4 - i] < hand_2[1][4 - i]:
				return 2
			else:
				return 0
# Import the words from the text file
with open("./poker.txt","r") as f:
    h = [s for s in f.read().split('\n')]

rounds = [ [[x[3*n:3*n + 2] for n in range(5)], [x[3*n:3*n + 2] for n in range(5, 10)]] for x in h ]

wins = [0, 0]

for r in rounds:

	winner = compare_hands(test_hand(r[0]), test_hand(r[1]))
	
	print r, str(test_hand(r[0])[0]).zfill(2), str(test_hand(r[1])[0]).zfill(2), winner

	if winner == 1:
		wins[0] += 1
	elif winner == 2:
		wins[1] += 1
	elif winner == 0:
		print 'error'

print wins
print "Finished in ", time.time() - start_time, "seconds"
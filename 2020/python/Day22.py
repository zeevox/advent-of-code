import aoc_utils


def parse(inp):
    decks = []
    for player in inp.strip().split("\n\n"):
        deck = [int(card) for card in player.splitlines()[1:]]
        decks.append(deck)
    return decks


# calculate the score of a given deck
def score(deck):
    # the bottom card in their deck is worth the value of the card multiplied by 1,
    # the second-from-the-bottom card is worth the value of the card
    # multiplied by 2, and so on.
    return sum(i * deck.pop(0) for i in range(len(deck), 0, -1))


def combat_round(deck1, deck2, game, out=False, game_count=1):
    if out:
        print(f"\n-- NEW ROUND (GAME {game_count}) --")

    # if there was a previous round in this game that had exactly the same cards in the
    # same order in the same players' decks, the game instantly ends in a win
    # for player 1
    if game is not None and (tuple(deck1), tuple(deck2)) in game:
        deck2 = []
    # otherwise, this round's cards must be in a new configuration
    else:
        if game is not None:
            game.add((tuple(deck1), tuple(deck2)))

        if out:
            print(f"{deck1=}\n{deck2=}")

        # the players begin the round by each drawing the top card of their
        # deck as normal.
        card1, card2 = deck1.pop(0), deck2.pop(0)

        if out:
            print(f"{card1=}\n{card2=}")

        winner = 1 if card1 > card2 else 2

        # if both players have at least as many cards remaining in their deck as
        # the value of the card they just drew, the winner of the round is determined
        # by playing a new game of Recursive Combat
        if game is not None and card1 <= len(deck1) and card2 <= len(deck2):
            if out:
                print("Playing a sub-game to determine the winner...")
            winner = play_game(
                deck1[:card1], deck2[:card2], False, out, game_count + 1
            )

        if out:
            print(f"Player {winner} wins this round of game {game_count}")
        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return deck1, deck2, game


def play_game(deck1, deck2, part1, out=False, game_count=1):
    if out:
        print(f"\n=== NEW GAME (GAME {game_count}) ===")

    # set game to None if this is part 1
    # that way it will not recurse
    game = None if part1 else set()
    while deck1 and deck2:
        deck1, deck2, game = combat_round(deck1, deck2, game, out, game_count)

    if game_count == 1:
        if not deck1:
            print(score(deck2))
        else:
            print(score(deck1))

    return 1 if deck1 else 2


inp = aoc_utils.input().read()

# we must assume that the input always has two players' decks
# although there is no validation that the input is such
deck1, deck2 = parse(inp)
play_game(deck1, deck2, True, False)

# parse it again because the decks will have been overwritten by part 1
deck1, deck2 = parse(inp)
play_game(deck1, deck2, False, False)

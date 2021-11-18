import Deck as dk
import Cards as ca


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")

        # create the deck from the Deck class
        self.deck = dk.Deck()
        # assigns the players
        self.p1 = Player(name1)
        self.p2 = Player("Dealer")

    def wins(self, winner):
        # just prints the winner
        w = f"{winner} wins"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        # just shows what was drawn
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")

        # We run while there are cards in the deck
        while len(cards) >= 2:

            # menu text
            m = "q to quit. Any " + \
                "key to play:"

            # wait for input
            response = input(m)
            if response == 'q':
                break

            # This is the draws
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()

            # moves the names over from other class
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)

            # Win counter
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        # End of loop
        win = self.winner(self.p1, self.p2)
        print("War is over.{} wins".format(win))

    def winner(self, p1, p2):

        # This is the end of the game, who is winner overall
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


# This is the game runner
if __name__ == "__main__":
    game = Game()
    game.play_game()

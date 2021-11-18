import Cards as ca


def askforname():
    name = str(input("Name: "))
    return name


def draw(x, playersum=None, dealersum=None):
    card = ca.getcard(x)

    if playersum is not None and dealersum is not None:
        if playersum > 21 and 11 in card or dealersum > 21 and 11 in card:
            index = 0
            for i in card:
                if i == 11:
                    card[index] = 1
                else:
                    index += 1

    return card


def status(dealer, player, pname):
    tdealer = sum(dealer)
    tplayer = sum(player)
    m = f"Dealer has  {tdealer} as {dealer}, " \
        f"{pname} has {tplayer} as {player}"
    print(m)


def main(playername, dl):
    # first draw
    dealercards = draw(1)
    playercards = draw(2)

    # Show the user
    status(dealercards, playercards, playername)

    if sum(playercards) == 21:
        print("That is BlackJack NICE!")
        print(f"{playername} WINS")
        return

    m = "Hit [h] or Stand [s]:" \
        " "
    done = False
    while not done:
        inplayer = str.lower(input(m))

        # if hit draw card
        if inplayer == "h":
            playercards += draw(1, sum(playercards), sum(dealercards))
            status(dealercards, playercards, playername)

            # check for bust
            if sum(playercards) > 21:
                print(f"{playername} that is a bust")
                return

            if sum(playercards) == 21:
                break

        # if stand draw for dealer
        elif inplayer == "s":
            done = True

        else:
            print("That is not a valid input, Try again")

    # Do the dealer
    while sum(dealercards) < 17:
        dealercards += draw(1, sum(playercards), sum(dealercards))
        status(dealercards, playercards, playername)

        # check for bust Dealer
        if sum(dealercards) > 21:
            print(f"That is a bust for the dealer, You WIN")
            return

    # Now we check who wins
    if sum(dealercards) > sum(playercards):
        print(f"{dl} wins")
    elif sum(playercards) > sum(dealercards):
        print(f"{playername} wins")
    else:
        print("This is a tie")


if __name__ == "__main__":
    pl = askforname()
    dl = "Dealer"
    while True:
        print("")
        main(pl, dl)

over = False
bids = {}

def compare(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for name in bidding_dictionary:
        bid_amount = bidding_dictionary[name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name

    print(f"The winner is {winner} with a bid of {bid_amount}")

while not over:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    done = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    bids[name] = bid

    if done == "no":
        over = True
        compare(bids)
    elif done == "yes":
        print("\n" * 20)
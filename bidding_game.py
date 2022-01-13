bids = {}
bidding_finished = False


# The function which finds highest bidder

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"{winner} is the winner with ${highest_bid}.")


while not bidding_finished:
    name = input("What's your name? ")
    price = input("What's your bid $")
    bids[name] = price
    should_continue = input("Are there any other bidders? yes or no")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    else:
        bidding_finished = False
import os
def bid_winner(bidder_info):
    highest_bid=0
    winner=""
    for bidder in bidder_info:
        bid_amount=bidder_info[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner}")

bidder_data={}
while True:
    name=input("The bidder's name: ")
    bid=float(input("The bidder's amount: "))
    bidder_data[name]=bid
    more_bidders=input("Is there any other bidder's? Type yes or no: ").lower()
    if more_bidders=='no':
        bid_winner(bidder_data)
        break
    elif more_bidders=='yes':
        os.system('cls')
        
import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
bidding_finished = False

def finding_bidder(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount>highest_bidder:
            highest_bidder= bidding_amount
            winner= bidder    
    print(f"The winner is {winner} with highest bid of ${highest_bidder}")

while not bidding_finished:
    name = input("Enter your name:  ")
    price = int(input("Enter your bidding price:  "))
    bids[name] = price
    should_continue = input("if you have more people to bid please type 'y' for yes and 'n' for no:  ").lower()
    if should_continue=="n":
        bidding_finished = True
        finding_bidder(bids)
    elif should_continue=="y":
        os.system('cls') 

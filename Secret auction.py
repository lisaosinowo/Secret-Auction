print("Welcome to the secret auction program.")

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
empty_bid = {}

def secret_auction(name, bid):
    empty_bid[name] = bid


any_bidders = True
while any_bidders == True:
    name_input = input("What is your name? ")
    bid_input = int(input("What is your bid? "))
    secret_auction(name_input, bid_input)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if other_bidders == "no":
        any_bidders = False

highest_number = []
for bids in empty_bid:
    bid_list = empty_bid[bids]
    highest_number.append(bid_list)

winning_bid = max(highest_number)

for person in empty_bid:
    if empty_bid[person] == winning_bid:
        winner = person

print(f"The winner is {winner} with a bid of £{winning_bid}!")

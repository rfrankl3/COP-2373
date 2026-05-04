def get_tickets_remaining(tickets_remaining):
    """
    Prompts user for number of tickets and validates input
    """
    while True:
        try:
            tickets = int(input("How many tickets would you like to purchase? (1-4): "))

            if tickets < 1 or tickets > 4:
                print("You can only buy between 1 and 4 tickets.")
            elif tickets > tickets_remaining:
                print("Not enough tickets remaining.")
            else:
                return tickets

        except ValueError:4
            print("Invalid input. Please enter a number.")


def sell_tickets():
    """
    Manages ticket selling process
    """
    tickets_remaining = 10
    buyer_count = 0

    while tickets_remaining > 0:
        print("\nTickets remaining:", tickets_remaining)

        tickets_bought = get_tickets_remaining(tickets_remaining)

        tickets_remaining = tickets_remaining - tickets_bought
        total_buyers = total_buyers + 1

        print("Purchase successful!")
        print("Tickets remaining after purchase:", tickets_remaining)

    print("\nAll tickets have been sold!")
    print("Total number of buyers:", total_buyers)


def main():
    sell_tickets()


if __name__ == "__main__":
    main()
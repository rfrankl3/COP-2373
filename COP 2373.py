def sell_tickets():
    remaining_tickets = 20
    total_buyers = 0
    while remaining_tickets > 0:
        print("\nTickets remaining:", remaining_tickets)
        tickets = int(input("Enter number of tickets to buy (1-4): "))
        if tickets >= 1 and tickets <= 4 and tickets <= remaining_tickets:
            remaining_tickets = remaining_tickets - tickets
            total_buyers = total_buyers + 1
            print("Tickets remaining after purchase:", remaining_tickets)
        else:
            print("Invalid number of tickets.")
    print("\nAll tickets sold out!")
    print("Total number of buyers:", total_buyers)

if __name__ == "__main__":
    sell_tickets()

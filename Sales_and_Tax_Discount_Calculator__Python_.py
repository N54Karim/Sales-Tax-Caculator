# Customer inputs for item quantity and state
item_number = input("Enter number of items: ")
item_number = int(item_number)

if item_number < 1:
    print("Count must be greater than zero")
else:
    valid_state = input("Enter a valid state (CA, NV, AZ): ").upper()

    # Branching path for different states
    if valid_state in ["CA", "NV", "AZ"]:
        # Calculate discount
        if item_number >= 20:
            discounted_cost = item_number * 0.9
            print("10% discount")
        elif item_number >= 10:
            discounted_cost = item_number * 0.95
            print("5% discount")
        else:
            discounted_cost = item_number
            print("No discount")

        # Display cost breakdown
        print(f"Gross cost:      {item_number:10.2f}")
        print(f"Discount:        {item_number - discounted_cost:12.2f}")
        print(f"Net cost:        {discounted_cost:12.2f}")

        # Tax calculation based on state
        tax_rates = {"CA": 0.20, "NV": 0.05, "AZ": 0.10}
        tax = discounted_cost * tax_rates[valid_state]

        print(f"Tax:            {tax:12.2f}")
        print(f"After tax:      {discounted_cost + tax:11.2f}")

    else:
        print("Invalid state")

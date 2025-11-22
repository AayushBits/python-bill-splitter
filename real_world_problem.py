def bill_splitter():
    item_names = []
    item_prices = []
    
    print("- bill splitter tool -")
    print("Enter your items. Type 'done' as the name when finished.\n")

    while True:
        name = input("item Name: ")
        if name.lower() == 'done':
            break
            
        try:
            price = float(input(f"Price for {name}: "))
        except ValueError:
            print("Invalid Please enter a number.")
            continue 

        item_names.append(name)
        item_prices.append(price)

    if len(item_prices) == 0:
        print("No items entered. exiting.")
        return

    tax_rate = float(input("\nenter tax rate %: "))
    tip_rate = float(input("enter tip % : "))
    people_count = int(input("how many people are splitting this?: "))

    subtotal = sum(item_prices)
    tax_amount = subtotal * (tax_rate / 100)
    tip_amount = subtotal * (tip_rate / 100)
    grand_total = subtotal + tax_amount + tip_amount
    per_person = grand_total / people_count

    print("\n" + "="*30)
    print("📄 final receipt")
    print("="*30)
    
    for i in range(len(item_names)):
        print(f"{item_names[i]:<20} ${item_prices[i]:.2f}")
    
    print("-" * 30)
    print(f"{'Subtotal:':<20} ${subtotal:.2f}")
    print(f"{'Tax:':<20} ${tax_amount:.2f}")
    print(f"{'Tip:':<20} ${tip_amount:.2f}")
    print("=" * 30)
    print(f"{'GRAND TOTAL:':<20} ${grand_total:.2f}")
    print("=" * 30)
    
    print(f"\neach person owes: ${per_person:.2f}")

bill_splitter()
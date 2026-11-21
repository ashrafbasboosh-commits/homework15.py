# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total_sales = 0

billing = True


# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    customer_name = input("Enter customer's name: ")
    item_count = int(input("How many items are they buying? "))

    # ---------- PART 3: continue on a bad item count ----------
    if item_count <= 0:
        print("Item count must be greater than 0. Skipping customer.\n")
        continue

    # ---------- PART 4: the INNER while loop — one item per repeat ----------
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        print(f"\nItem {item_number}:")
        item_name = input("  Enter item name: ")
        price = int(input("  Enter item price: "))
        quantity = int(input("  Enter item quantity: "))

        # ---------- PART 5: item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("  Price and quantity must be greater than 0. Please re-enter.")
            continue

        item_total = price * quantity
        print(f"  {item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    # ---------- PART 6: finish the customer, ask about the next ----------
    customers_served += 1
    total_sales += customer_total
    print(f"\nTotal for {customer_name}: {customer_total}\n")

    next_customer = input("Next customer? (yes/no): ").strip().lower()
    if next_customer != "yes":
        billing = False
    print()


# ---------- PART 7: the NESTED for report ----------
print("=== Daily Summary Report ===")
bands = [
    ("Low price (< 50)     : ", low_price_items),
    ("Medium price (50-100): ", medium_price_items),
    ("High price (> 100)   : ", high_price_items),
]

for label, count in bands:
    print(label, end="")
    for _ in range(count):
        print("*", end="")
    print()

print(f"\nCustomers served: {customers_served}")
print(f"Total sales: {total_sales}")

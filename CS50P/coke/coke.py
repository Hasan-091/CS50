# Variable to keep track
amount_due = 50

# Loop forever until we break at some point
while amount_due > 0:
    print("Amount Due:", amount_due)

    coin_inserted = int(input("Insert Coin: "))

    if coin_inserted in [25, 10, 5]:
        amount_due -= coin_inserted


change_owed = abs(amount_due)
print("Change Owed:", change_owed)

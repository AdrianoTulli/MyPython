cost = 50

while cost > 0 :
    print("Amount Due:", cost)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        cost -= coin
if cost < 0: cost = -cost

print("Change Owed:", cost)

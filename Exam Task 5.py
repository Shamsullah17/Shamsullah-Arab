print("Enter item price")
item_price = int(input())
print("Enter how much paid")
how_much_paid = int(input())
amount = how_much_paid - item_price
d = []
while amount > 0:
    if amount >= 20:
        amount = amount-20
        d.append(20)
    else:
        if amount >= 10:
            amount = amount-10
            d.append(10)
        else:
            if amount >= 5:
                amount = amount-5
                d.append(5)
            else:
                if amount >= 2:
                    amount = amount-2
                    d.append(2)
                else:
                    if amount >= 1:
                        amount = amount-1
                        d.append(1)
                    else:
                        print("Something went wrong")
for i in range(0, len(d)):
    print(d[i])

# Hotel project

"""
1. Menus
2. quantity & amount
3. offer discount
"""

import datetime
print("********** Welcome to AK Hotel *********")

menus = ["dhosa", "chappathi", "briyani"]
print("Avilable menus are", menus)

dhosa_amount = 15
chappathi_amount = 25
briyani_amount = 120

user_order = input("Enter your order : ").lower()

if user_order in menus:
    print(f"{user_order} is available")
    how_many = int(input(f"How many {user_order} you want : "))
    if user_order == "dhosa":
        total = how_many*dhosa_amount
        print(
            f"one dhosa amount is {dhosa_amount} you order {how_many} dhosa and your total bill is {total}")
        if total >= 1000:
            print("200rs discount for diwali offer")
            offer_amount = total-200
            print(f"Final price is {offer_amount}")
            date = datetime.datetime.now()
            bill = input("Do you want bill type yes : ")
            if bill == "yes":
                f = open("bill.txt", "w")
                f.write(
                    f"your total bill is {offer_amount} \nBill genrated on {date}")
                print("bill genrated Successfully")

    elif user_order == "chappathi":
        total = how_many*chappathi_amount
        print(
            f"one chappathi amount is {chappathi_amount} you order {how_many} and your total bill is {total}")
        if total >= 1500:
            print(f"200rs discount for diwali offer")
            offer_amount = total-200
            print(f"your final price is {offer_amount}")
            date = datetime.datetime.now()
            bill = input("Do you want bill type yes : ")
            if bill == "yes":
                f = open("bill.txt", "w")
                f.write(
                    f"your total bill is {offer_amount} \nBill genrated on {date}")
                print("bill genrated Successfully")
    elif user_order == "briyani":
        total = how_many*briyani_amount
        print(
            f"one briyani amount is {briyani_amount} you order {how_many} and your total bill is {total}")
        if total >= 2000:
            print("200rs discount for diwali offer")
            offer_amount = total-300
            print(f"your final price is {offer_amount}")
            date = datetime.datetime.now()
            bill = input("Do you want bill type yes : ")
            if bill == "yes":
                f = open("bill.txt", "w")
                f.write(
                    f"your total bill is {offer_amount} \nBill genrated on {date}")
                print("bill genrated Successfully")
else:
    print(f"{user_order} is not available")
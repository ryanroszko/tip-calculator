print("Welcome to the tip calculator.")
bill_total = float(input("What is the total bill?: $"))
tip = int(input("What tip percentage would yopu like to leave?: "))
split = int(input("How people are splitting the bill?: "))

total_with_tip = round(bill_total * (tip / 100 + 1), 2)

per_person = round(total_with_tip / split, 2)
print(f"Each person should pay ${per_person:.2f}")

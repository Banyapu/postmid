MIN_AMOUNT = 500
CASHBACK_T = 5
CASHBACK_R = 10
MIN_DIFF = 0.4

liters = int(input("Total Liters: "))
yp = float(input("Yesterday price (Bath/Liters): "))
tp = float(input("Today price (Bath/Liters): "))

MSG = "Enter payment method (r for reward, t for travel, c for cash): "
E_MSG = 'Error incorrect "Payment method"'

pay_method = input(MSG)
while pay_method != "r" or pay_method != "t" or pay_method != "c":
    print(E_MSG)
    pay_method = input(MSG)

total_amount = liters * tp
if total_amount < MIN_AMOUNT:  # <500
    cashback = 0
else:
    if pay_method == "c":
        cashback = 0
    elif pay_method == "t":
        cashback = CASHBACK_T  # = 5
    else:
        cashback = CASHBACK_R  # = 10
diff = tp - yp

if diff >= MIN_DIFF:  # 40 สตางค์ / ลิตร
    reward = 3 * liters
elif diff <= 0:
    reward = liters
else:
    reward = 2 * liters

total_paid = total_amount - cashback
print(f"Total amount: {total_amount:.2f} bath")
print(f"Cashback: {cashback:.2f} bath")
print(f"Total paid: {total_paid:.2f}")
print(f"Reward: {reward}")

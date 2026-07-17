name = "Alex"
quantity = 5
price = 10.5
is_vip = True

subtotal = quantity * price
discount = 5.0 if is_vip else 0.0
total = subtotal - discount


def evaluate_score(score):
    if score >= 90:
        return "Pass with distinction"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


scores = [95, 78, 42]

for s in scores:
    result = evaluate_score(s)
    print(f"Score {s}: {result}")

count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print(f"Final total for {name}: ${total}")

number = int(input("შეიყვანეთ რიცხვი: "))


if number > 100 or number % 9 == 0:
    print(f"რიცხვი {number} არის 100-ზე მეტი და 9-ის ჯერადი.")
else:
    print(f"რიცხვი {number} არ არის 100-ზე მეტი ან არ არის 9-ის ჯერადი.")
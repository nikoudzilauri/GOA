num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))


print("ოპერაციები:")
print("1. მიმატება")
print("2.  გამოკლება")
print("3. გამრავლება")
print("4. გაყოფა")
print("5. ხარისხის ამოღება")
print("6. ღრმა ნამრავლი")

choice = input("აირჩიეთ ოპერაცია (1-6): ")

if choice == '1':
    result = num1 + num2
    print("შედეგი: ", result)
elif choice == '2':
    result = num1 - num2
    print("შედეგი: ", result)
elif choice == '3':
    result = num1 * num2
    print("შედეგი: ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("შედეგი: ", result)
    else:
        print("შეცდომა: არა შეიძლება გაყოფა 0-ზე")
elif choice == '5':
    result = (num1 + num2) / 2
    print("შედეგი: ", result)
elif choice == '6':
    result = num1 ** 0.5
    print("შედეგი: ", result)
else:
    print("შეცდომა: შეცდომა არასწორი ოპერაცია")
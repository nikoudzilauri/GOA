ticket = 10
user = int(input("how many tickets you want buy? "))

if user < 5 :
    print(ticket * user)
else:
        dis = user * ticket * 0.7
        print(dis)
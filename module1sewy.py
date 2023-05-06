history = [
    "ალბერტ აინშტაინი", "ყველაზე ჭკვიანი ადამიანი",
    "ანტონიო მეუცი", "ადამიანი რომელმაც შექმნა ტელეფონი 1859 წელს",
    "ტიმ ბერნერს-ლი", "ადამიანი რომელმაც შექმნა ინტერნეტი 1989 წელს"
]
print(history)


while True:
    operation = input("აირჩიეთ ოპერაცია: 1 - დამატება, 2 - წაშლა, 3 - ბეჭდვა, 4 - დათვლა")

    if operation == "1":
        add = input("ვისი დამატება გინდა?")
        history.append(add)

    elif operation == "2":
        more = input("ვისი წაშლა გინდა?")
        if more in history:
            history.remove(more)
        else:
            print("ვერ მოიძებნა")

    elif operation == "3":
        print(history)

    elif operation == "4":
        sui = len(history)
        print(sui)

    else:
        print("არასწორი ოპერაცია")









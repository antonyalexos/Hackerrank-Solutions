num = int(raw_input())

phone_book = {}

for i in range(0, num):
    entry = str(raw_input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(raw_input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
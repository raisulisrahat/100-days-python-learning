# Here I am showing Day 12 to Day 14 python practise

# 12 | Inheritance
# 13 | Polymorphism
# 14 | Iterator 

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class PhoneList:
    def __init__(self):
        self.phones = []
        self.index = 0

    def add_phone(self, phone):
        self.phones.append(phone)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.phones):
            phone = self.phones[self.index]
            self.index += 1
            return phone
        raise StopIteration

brand = ("Blackberry", "Samsung", "Iphone", "Sony", "Xiaomi", "Realme", "Opp")
price = ("$1000", "$1100", "$1200", "$900", "$500", "$300", "$400")
model = ("A1", "S20+", "14 pro", "XZ22", "Note 15", "C3", "H6")

phone_list = PhoneList()

for i in range(len(brand)):
    new_phone = Phone(brand[i], model[i], price[i])
    phone_list.add_phone(new_phone)

for phone in phone_list:
    print("Brand:", phone.brand)
    print("Model:", phone.model)
    print("Price:", phone.price)
    print()

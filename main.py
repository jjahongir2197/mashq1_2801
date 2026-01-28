class Medicine:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def info(self):
        return f"{self.name} | {self.price} so‘m | Qoldiq: {self.qty}"


class Pharmacy:
    def __init__(self):
        self.medicines = []
        self.income = 0

    def add_medicine(self, m):
        self.medicines.append(m)

    def show(self):
        for i, m in enumerate(self.medicines):
            print(i, m.info())

    def sell(self, index, amount):
        m = self.medicines[index]
        if m.qty >= amount:
            m.qty -= amount
            self.income += m.price * amount
            print("Sotildi")
        else:
            print("Yetarli dori yo‘q")

    def report(self):
        print("Daromad:", self.income)


ph = Pharmacy()
ph.add_medicine(Medicine("Paracetamol", 3000, 50))
ph.add_medicine(Medicine("Vitamin C", 5000, 30))

while True:
    print("\n1.Dorilar 2.Sotish 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        ph.show()
    elif c == "2":
        ph.sell(int(input("Index: ")), int(input("Soni: ")))
    elif c == "3":
        ph.report()
    elif c == "0":
        break

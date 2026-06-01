import random

class OrderDataHelper:
    @staticmethod
    def generate_order_data():
        names = ["Илья", "Дима", "Леонид", "Алексей", "Денис"]
        surnames = ["Тихонов", "Коньков", "Олейников", "Фирсов", "Приветов"]
        name = random.choice(names)
        surname = random.choice(surnames)
        address = f"Москва, ул. Теплый Стан, д. {random.randint(10, 30)}"
        metro = "Беляево"
        phone = f"79{random.randint(100000000, 999999999)}"
        date = f"{random.randint(10, 28)}.{random.randint(10, 12)}.2026"
        rent_period = "сутки"
        comment = "комментарий"
        return name, surname, address, metro, phone, date, rent_period, comment
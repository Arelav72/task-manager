class Task:
    def __init__(self, description, deadline, status=False):
        # Инициализация экземпляра класса `Task` с параметрами описания, дедлайна, и статуса задачи (статус по умолчанию - False).
        self.description = description  # Описание задачи.
        self.deadline = deadline  # Дедлайн выполнения задачи.
        self.status = status  # Текущее состояние задачи, не выполнена (False) или выполнена (True).

    def mark_as_done(self):
        # Метод для отметки задачи как выполненной.
        self.status = True

    def __str__(self):
        # Метод для возвращения строкового представления объекта класса `Task`.
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {'Выполнено' if self.status else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        # Инициализируется объект Менеджер задач  без задач.
        self.tasks = []  # Пустой список для хранения задач

    def add_task(self, task):
        # Добавление задачи в список задач
        self.tasks.append(task)

    def mark_done(self, description):
        # Поиск и отметка выполненной задачи по описанию.
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                break  # Прерываем цикл при нахождении первого совпадения

    def show_tasks(self):
        # Возвращает список невыполненных задач
        return [task for task in self.tasks if not task.status]


class Store:
    def __init__(self, name, address):
        # Инициализация объекта магазина с названием и адресом.
        self.name = name  # Название магазина.
        self.address = address  # Адрес магазина.
        self.items = {}  # Словарь для хранения товаров и их цен.

    def add_item(self, item_name, price):
        # Добавление товара и его цены в словарь товаров магазина.
        self.items[item_name] = price

    def remove_item(self, item_name):
        # Удаляет товар из словаря по его имени, если он найден.
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        # Возвращает цену товара по его имени, если товар найден, иначе - None.
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        # Обновление цены товара, если товар найден в словаре.
        if item_name in self.items:
            self.items[item_name] = new_price

store1 = Store("Пяторочка", "Улица Пионерская 24")
store2 = Store("Магнит", "Улица Ватутина 132")
store3 = Store("Лента", "Улица Московская 12")

store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store2.add_item("Хлеб", 1.0)
store2.add_item("Молоко", 0.9)
store3.add_item("Чай", 0.5)
store3.add_item("Шоколад", 0.9)

store1.update_price("Яблоки", 0.55)
print('В Пятерочке цена на яблоки ', store1.get_price("Яблоки"))

store2.remove_item("Хлеб")
print('Хлеб в Магните - ', store2.get_price("Хлеб"))  # None, потому что хлеб был удален

print('Cписок продуктов в Ленте:', store3.items)
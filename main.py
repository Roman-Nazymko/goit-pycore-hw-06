from collections import UserDict

"""Базовий клас для полів запису"""
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

"""Клас для зберігання імені контакту. Обов'язкове поле."""
class Name(Field):
    def __init__(self, name):
          self.value = name

"""Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""
class Phone(Field):
    def __init__(self, phone):
         self.value = self.validate_phone_number(phone)
    
    def validate_phone_number(self, phone):
         if len(phone) != 10:
              raise ValueError("Phone number must be a string of 10 digits.")
         if not phone.isdigit():
              raise ValueError("The phone number must contain only numbers")

         return phone 


"""Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів."""
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    #Додавання телефонів
    def add_phone(self, phone):
         self.phones.append(Phone(phone))
    
    #Видалення телефонів
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print(f"Phone number '{phone}' removed successfully.")
                break
        else:
            print(f"No phone number '{phone}' found.")
    
    #Редагування телефонів
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                print(f"Phone number '{old_phone}' edited successfully to '{new_phone}'.")
                break
        else:
            print(f"No phone number '{old_phone}' found.")

    #Пошук телефону
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return phone
        return None
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    # Додавання записів
    def add_record(self, record):
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    #Пошук записів за іменем
    def find(self, name):
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' not found.")
        return record
    
    #Видалення записів за іменем
    def delete(self, name):
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]




# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
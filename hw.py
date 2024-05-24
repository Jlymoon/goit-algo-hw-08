import pickle


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def list_contacts(self):
        return self.contacts.items()


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    while True:
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Показати контакт")
        print("4. Показати всі контакти")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            address = input("Введіть адресу: ")
            book.add_contact(name, address)
        elif choice == "2":
            name = input("Введіть ім'я контакту, який потрібно видалити: ")
            book.remove_contact(name)
        elif choice == "3":
            name = input("Введіть ім'я контакту: ")
            contact = book.get_contact(name)
            if contact:
                print(f"Адреса: {contact}")
            else:
                print("Контакт не знайдено.")
        elif choice == "4":
            contacts = book.list_contacts()
            for name, address in contacts:
                print(f"{name}: {address}")
        elif choice == "5":

            save_data(book)
            print("Дані збережено. Вихід з програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз!")


if __name__ == "__main__":
    main()
1
class ContactBot:
    def __init__(self):
        self.contacts = {}

    def hello(self):
        return "How can I help you?"

    def add_contact(self, username, phone):
        self.contacts[username] = phone
        return f"Contact {username} added with phone {phone}."

    def change_contact(self, username, phone):
        if username in self.contacts:
            self.contacts[username] = phone
            return f"Phone number updated for {username}."
        else:
            return f"Contact {username} not found."

    def get_phone(self, username):
        if username in self.contacts:
            return f"The phone number for {username} is {self.contacts[username]}."
        else:
            return f"Contact {username} not found."

    def get_all_contacts(self):
        if self.contacts:
            result = "All contacts:\n"
            for username, phone in self.contacts.items():
                result += f"{username}: {phone}\n"
            return result
        else:
            return "No contacts available."

    def close(self):
        return "Good bye!"


def main():
    bot = ContactBot()
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print(bot.hello())
        elif command.startswith("add"):
            _, username, phone = command.split()
            print(bot.add_contact(username, phone))
        elif command.startswith("change"):
            _, username, phone = command.split()
            print(bot.change_contact(username, phone))
        elif command.startswith("phone"):
            _, username = command.split()
            print(bot.get_phone(username))
        elif command == "all":
            print(bot.get_all_contacts())
        elif command in ["close", "exit"]:
            print(bot.close())
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
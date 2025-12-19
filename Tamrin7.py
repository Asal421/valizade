class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("شماره تلفن باید فقط عدد باشد")
        self.name = name
        self.phone_number = phone_number


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def save_to_csv(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number}\n")

    def load_from_csv(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        name, phone = line.strip().split(",")
                        contact = Contact(name, phone)
                        self.contacts.append(contact)
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("📂 فایل یافت نشد، دفترچه تلفن جدید ایجاد شد")


def main():
    phonebook = PhoneBook()
    filename = "contacts.csv"

    phonebook.load_from_csv(filename)

    while True:
        print("\n سیستم مدیریت مخاطبین")
        print("1. افزودن مخاطب")
        print("2. نمایش همه مخاطبین")
        print("3. ذخیره و خروج")

        try:
            choice = int(input("انتخاب شما: "))
        except ValueError:
            print(" لطفاً عدد وارد کنید")
            continue

        if choice == 1:
            name = input("نام مخاطب: ")
            phone = input("شماره تلفن: ")

            try:
                phonebook.add_contact(name, phone)
                print(" مخاطب با موفقیت اضافه شد")
            except ValueError:
                print(" فرمت شماره اشتباه است، دوباره تلاش کنید")

        elif choice == 2:
            if not phonebook.contacts:
                print(" هیچ مخاطبی ثبت نشده است")
            else:
                print("\n لیست مخاطبین:")
                for c in phonebook.contacts:
                    print(f"{c.name} - {c.phone_number}")

        elif choice == 3:
            phonebook.save_to_csv(filename)
            print(" اطلاعات ذخیره شد !")
            break

        else:
            print("❌ گزینه نامعتبر")


if __name__ == "__main__":
    main()

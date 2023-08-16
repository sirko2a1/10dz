class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]

    def search_by_name(self, name):
        if name in self.data:
            return self.data[name]

    def search_by_phone(self, phone):
        for record in self.data.values():
            if any(p.value == phone for p in record.phones):
                return record

    def __str__(self):
        records_str = "\n".join(str(record) for record in self.data.values())
        return records_str


if __name__ == "__main__":
    book = AddressBook()

    record1 = Record("John Doe")
    record1.add_phone("123-456-7890")
    record1.add_phone("987-654-3210")
    book.add_record(record1)

    record2 = Record("Jane Smith")
    record2.add_phone("555-123-4567")
    book.add_record(record2)

    print("Address Book:")
    print(book)

    print("\nSearching by name:")
    found_record = book.search_by_name("John Doe")
    if found_record:
        print(found_record)
    else:
        print("Record not found.")

    print("\nSearching by phone:")
    found_record = book.search_by_phone("555-123-4567")
    if found_record:
        print(found_record)
    else:
        print("Record not found.")

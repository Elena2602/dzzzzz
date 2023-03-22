phone_book = []
path = 'phone.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

def change_contact(contact: dict, index: int):
    phone_book.pop(index - 1)
    phone_book.insert(index - 1, contact)


def delete_contact(ind: int):
    global phone_book
    phone_book.pop(ind -1)

def find_contact(search: str) ->  list[dict]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result


